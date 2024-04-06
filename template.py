import os
from pathlib import Path

file_path_str = 'C:/Users/Krishna.Arjun/Desktop/Krish/iNeuron/Practice work/Restaurent project'
package_name = "RestuarantClassification"


list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/utils.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep"
]
for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename=os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")



print("Filename:", file_path.name)
print("Directory:", file_path.parent)