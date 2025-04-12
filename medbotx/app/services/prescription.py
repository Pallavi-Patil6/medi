from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('app/templates'))

def generate_prescription(name, age, symptoms, diagnosis):
    template = env.get_template("prescription_template.html")
    return template.render(name=name, age=age, symptoms=", ".join(symptoms), diagnosis=diagnosis)
