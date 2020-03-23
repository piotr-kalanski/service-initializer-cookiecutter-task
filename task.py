import logging
from cookiecutter.main import cookiecutter


def run_task(name: str, description: str, parameters: dict, service_metadata: dict):
    logging.info("Generating project directory using cookiecutter")

    template_url_field_name = parameters['template_url_field_name']
    parameters_field_name = parameters['parameters_field_name']
    output_dir = parameters['output_dir']

    template_url = service_metadata[template_url_field_name]
    parameters = service_metadata[parameters_field_name]

    cookiecutter(
        template=template_url,
        no_input=True,
        extra_context=parameters,
        output_dir=output_dir,
    )

    logging.info(f"Generated project directory using cookiecutter from template {template_url}")
