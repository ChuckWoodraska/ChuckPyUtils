import stringcase


def data_formatter(data_dict, form_data):
    for k in data_dict:
        data_dict[k] = form_data.get(stringcase.camelcase(k), data_dict[k])
    return data_dict


def transform_checkbox(checkbox):
    """Transform checkbox return value from JavaScript."""
    return checkbox == 'on'


def transform_boolean(bool_value):
    """Transform boolean return value from JavaScript."""
    return bool_value == 'true'
