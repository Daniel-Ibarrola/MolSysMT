from importlib import import_module
import os

forms = []

dict_type = {}
dict_info = {}
dict_elements = {}
dict_attributes = {}
dict_is_form = {}
dict_extract = {}
dict_add = {}
dict_merge = {}
dict_append_frames = {}
dict_concatenate_frames = {}
dict_get = {}
dict_set = {}
dict_convert = {}

#file_extensions_recognized = []
#string_names_recognized = []

current_dir = os.path.dirname(os.path.abspath(__file__))
list_apis = [filename.split('.')[0] for filename in os.listdir(current_dir) if filename.startswith('api_')]

for api_name in list_apis:

    mod = import_module('molsysmt.api_forms.'+api_name)

    forms.append(mod.form_name)

    dict_type[mod.form_name]=mod.form_type
    dict_info[mod.form_name]=mod.form_info
    dict_elements[mod.form_name]=mod.form_elements
    dict_attributes[mod.form_name]=mod.form_attributes

    dict_is_form[mod.form_name]=mod.is_form
    dict_add[mod.form_name]=mod.add
    dict_merge[mod.form_name]=mod.merge
    dict_append_frames[mod.form_name]=mod.append_frames
    dict_concatenate_frames[mod.form_name]=mod.concatenate_frames
    dict_extract[mod.form_name]=mod.extract

    dict_convert[mod.form_name]= {}
    dict_get[mod.form_name]= {'atom':{}, 'group':{}, 'component':{}, 'molecule':{}, 'chain':{},
                          'entity':{}, 'system':{}, 'bond':{}}
    dict_set[mod.form_name]= {'atom':{}, 'group':{}, 'component':{}, 'molecule':{}, 'chain':{},
                          'entity':{}, 'system':{}, 'bond':{}}

    for method in mod.__dict__.keys():
        if method.startswith('to_'):
            if method.startswith('to_string_'):
                out_form_name=method.replace('to_string_','string:')
            elif method.startswith('to_file_'):
                out_form_name=method.replace('to_file_','file:')
            else:
                out_form_name=method.replace('to_','').replace('_','.',1)
            dict_convert[mod.form_name][out_form_name]= getattr(mod, method)
        if method.startswith('get_'):
            option, target = method[4:].split('_from_')
            dict_get[mod.form_name][target][option]=getattr(mod, method)
        if method.startswith('set_'):
            option, target = method[4:].split('_to_')
            dict_set[mod.form_name][target][option]=getattr(mod, method)

    #if mod.form_type=='file':
    #    file_extensions_recognized.append(mod.form_name.split(':')[-1].lower())
    #elif mod.form_type=='string':
    #    string_names_recognized.append(mod.form_name.split(':')[-1])

del(mod, method, out_form_name)
del(list_apis, current_dir, import_module)

