
# Digital Twin Technology by Tensornetics LLC

This repository contains the code for a digital twin technology solution built by Tensornetics LLC. The technology integrates the OpenAI API and NVIDIA NEMO for ASR, NLP, and TTS, along with RIVA for ASR.

## Requirements
The following packages are required to run the technology:

- openai
- nvidia-nemo
- riva

These packages can be installed using pip by running the following command:
```
pip install -r requirements.txt
```

## Deployment

The deployment of the technology is managed using Kubernetes. The deployment specifications are defined in the deployment folder. The kustomization.yaml file is used to configure and manage the deployment.

```
digital-twin-technology
|-- api/
|   |
|   |-- openai/
|   |   |
|   |   |-- openai_api.py 
|   |   |-- openai_config.py 
|   |
|   |-- nvidia/
|   |   |
|   |   |-- nemo/
|   |   |   |
|   |   |   |-- nemo_asr.py 
|   |   |   |-- nemo_nlp.py 
|   |   |   |-- nemo_tts.py 
|   |   |
|   |   |-- riva/
|   |   |   |
|   |   |   |-- riva_asr.py 
|   |
|-- main/
|   |
|   |-- ai_assistant.py 
|   |-- main.py 
|
|-- tests/
|   |
|   |-- test_ai_assistant.py 
|
|-- deployment/
|   |
|   |-- kubernetes/
|   |   |
|   |   |-- kustomization.yaml 
|   |   |-- deployment.yaml 
|   |   |-- service.yaml 
|   |   |-- ingress.yaml 
|   |   |-- istio/ (folder to store ISTIO related configuration files)
|   |
|-- requirements.txt 
|-- README.md
```
