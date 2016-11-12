import functools

from pyramid.httpexceptions import HTTPSeeOther

def require_prior_steps(fn):
    @functools.wraps(fn)
    def inner(self):
        if self.current_step not in self.allowed_steps:
            raise HTTPSeeOther(
                location=self.request.route_path(self.next_route)
            )

        return fn(self)
    return inner

class MultistepMixin(object):
    # Store multistep form data under this session key
    session_key = 'multistep_form'

    @property
    def steps(self):
        raise NotImplementedError

    @property
    def current_step(self):
        current_route_name = self.request.matched_route.name

        for key, route, name in self.steps:
            if route == current_route_name:
                return (key, route, name)

        return None

    @property
    def allowed_steps(self):
        for key, route, name in self.steps:
            yield (key, route, name)

            if key not in self.session_data:
                return

    @property
    def next_step(self):
        for key, route, name in self.steps:
            if key not in self.session_data:
                return (key, route, name)

        return None

    @property
    def next_route(self):
        _, route, _ = self.next_step

        return route

    @property
    def session_data(self):
        return self.request.session.setdefault(self.session_key, {})

    def persist(self, data, key=None):
        if key == None:
            key, route, name = self.current_step

        self.session_data[key] = data
        self.request.session.changed()

    def clear(self):
        self.request.session.pop(self.session_key, None)
        self.request.session.changed()
