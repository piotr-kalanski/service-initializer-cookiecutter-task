# service-initializer-cookiecutter-task

[Service Initializer](https://github.com/piotr-kalanski/service-initializer) task generating project template using cookiecutter.

# Run command

    docker run -it --rm -v OUTPUT_DIRECTORY:/output piotrkalanski/service-initializer-cookiecutter-task --name service_name --description service_description --parameters "{'template_url_field_name':'template_url','output_dir':'/output/','parameters_field_name':'params'}" --service-metadata "{'template_url':COOKIECUTTER_TEMPLATE_URL,'params':COOKIECUTTER_TEMPLATE_PARAMETERS"

Example:

    docker run -it --rm -v C:\generated_project:/output piotrkalanski/service-initializer-cookiecutter-task --name service_name --description service_description --parameters "{'template_url_field_name':'template_url','output_dir':'/output/','parameters_field_name':'params'}" --service-metadata "{'template_url':'https://github.com/audreyr/cookiecutter-pypackage.git','params':{}}"
