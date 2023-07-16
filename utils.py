import yaml

def read_yaml(config_path):
    try:
        with open(config_path, "r") as config:
            config_data = yaml.safe_load(config)
        return config_data
    except Exception as e:
        return {"error": str(e)}

config_loader = read_yaml(f"config.yaml")


from pptx import Presentation
import os
import uuid
import shutil
def ppt_to_pdf(input_file, output_file):
    presentation = Presentation(input_file)
    presentation.export(output_file)

if os.path.exists("ppt_to_pdf_dirs"):
    shutil.rmtree("ppt_to_pdf_dirs")
pdf_data_file=f"{str(uuid.uuid1())[:4]}.pdf"
os.makedirs("ppt_to_pdf_dirs")
input_file = "samplepptx.pptx"
output_file =f"ppt_to_pdf_dirs/{pdf_data_file}"
ppt_to_pdf(input_file, output_file)
