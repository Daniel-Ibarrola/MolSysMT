from molsysmt.api_forms import forms
from molsysmt._private_tools.lists_and_tuples import is_list_or_tuple
from molsysmt._private_tools.exceptions import *
from molsysmt.tools.form import is_file as form_is_file

form_from_lowercase = {ii.lower():ii for ii in forms}

def digest_form(form):

    if is_list_or_tuple(form):
        output = [digest_form(ii) for ii in form]
    else:
        output = form_from_lowercase[form.lower()]

    return output

def digest_to_form(to_form):

    if to_form is None:
        return None
    else:
        return digest_form(to_form)

