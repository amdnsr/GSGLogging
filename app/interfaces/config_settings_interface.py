from app.utils.helpers import pretty_text, remove_hidden_vars_fun_and_methods

class Config_Settings_Base():
    @classmethod
    def print(cls, boundary="=", boundary_length=100, separator="\n", indentation_text="\t"):
        class_name = cls.__name__
        dunder_dict = cls.__dict__
        class_variables = remove_hidden_vars_fun_and_methods(dunder_dict)
        key_value_dict = {class_variable: getattr(
            cls, class_variable) for class_variable in class_variables}
        text = pretty_text(class_name, key_value_dict, boundary,
                           boundary_length, separator, indentation_text)
        return text

    def load(self):
        raise NotImplementedError

