Pasos para ejecutar ejemplos:

docker build -t python-scikitlearn:1.0.0 .
docker run -t --rm -v $(pwd):/app python-scikitlearn:1.0.0 python class_1/NeuronalNetwork.py