import itertools
import logging

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther

from ..forms import (
    InformationForm,
    AddressForm,
    ContactForm
)
from ..mixin import MultistepMixin, require_prior_steps

log = logging.getLogger(__name__)

class MultistepFormView(MultistepMixin, object):
    steps = [
        ('info', 'multistep.information', 'Information'),
        ('address', 'multistep.address', 'Address'),
        ('contacts', 'multistep.contacts', 'Contacts'),
        (None, 'multistep.confirm', 'Confirm')
    ]


    def __init__(self, request):
        self.request = request

    @view_config(
        route_name='multistep.information',
        renderer='multistep/information.jinja2'
    )
    @require_prior_steps
    def information(self):
        form = InformationForm(
            self.request,
            self.request.POST,
            data=self.session_data.get('information', None)
        )

        if self.request.method == 'POST' and form.validate():
            # save data
            self.persist(form.data)
            return HTTPSeeOther(
                location=self.request.route_url(self.next_route)
            )


        return dict(
            form=form
        )

    @view_config(
        route_name='multistep.address',
        renderer='multistep/address.jinja2'
    )
    @require_prior_steps
    def address(self):
        form = AddressForm(
            self.request,
            self.request.POST,
            data=self.session_data.get('address', None)
        )
        if self.request.method == 'POST' and form.validate():
            # save data
            self.persist(form.data)
            return HTTPSeeOther(
                location=self.request.route_url(self.next_route)
            )

        return dict(
            form=form
        )

    @view_config(
        route_name='multistep.contacts',
        renderer='multistep/contacts.jinja2'
    )
    @require_prior_steps
    def contacts(self):
        form = ContactForm(
            self.request,
            self.request.POST,
            data=self.session_data.get('contacts', None)
        )
        if self.request.method == 'POST' and form.validate():
            self.persist(form.data)
            return HTTPSeeOther(
                location=self.request.route_url(self.next_route)
            )

        return dict(
            form=form
        )

    @view_config(
        route_name='multistep.confirm',
        renderer='multistep/confirm.jinja2'
    )
    @require_prior_steps
    def confirm(self):
        if self.request.method == 'POST':
            self.clear()

            raise HTTPSeeOther(
                location=self.request.route_url('index')
            )

        return dict(
            data=self.session_data,
            steps=self.steps
        )




@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {}


def includeme(config):
    config.scan(__name__)

    config.add_route('index', '/')

    config.add_route('multistep.information', '/information')
    config.add_route('multistep.address', '/address')
    config.add_route('multistep.contacts', '/contacts')
    config.add_route('multistep.confirm', '/confirm')
