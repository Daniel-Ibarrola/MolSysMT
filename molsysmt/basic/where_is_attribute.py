from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from molsysmt._private.lists_and_tuples import is_list_or_tuple

def where_is_attribute(molecular_system, attribute, check=True):

    from . import get_form, is_molecular_system
    from molsysmt.attribute.attributes import _reverse_search_in_molecular_system, _required_attributes
    from molsysmt.api_forms import dict_attributes
    from molsysmt.attribute import is_attribute

    if check:

        if not is_attribute(attribute):
            raise WrongAttributeError('attribute')

        if not is_molecular_system(molecular_system):
            raise SingleMolecularSystemNeededError()

    if not is_list_or_tuple(molecular_system):
        molecular_system = [molecular_system]

    forms_in = get_form(molecular_system)

    if _reverse_search_in_molecular_system[attribute]:
        aux_zip = zip(reversed(molecular_system), reversed(forms_in))
    else:
        aux_zip = zip(molecular_system, forms_in)

    output_item = None
    output_form = None

    for item, form_in in aux_zip:
        for required_attribute in _required_attributes[attribute]:
            if dict_attributes[form_in][required_attribute]:
                output_item = item
                output_form = form_in
                break
        if output_form is not None:
            break

    return output_item, output_form
