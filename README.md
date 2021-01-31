# k8s-flaskapp-with-nginx-proxy

A basic flask app that will be deployed in k8s behind a nginx which acts as a reverse-proxy.

## Getting Started

We will be building image first of app and then nginx and then will be deploying both on k8s cluster.

### Why nginx as reverse proxy?
As we know, we can also use nginx-ingress-controller in the cluster and also use cloud-provider ingress as well but when it comes to tweaking something to achieve next level of optimization and utilization then using our own nginx in front of app will give us the control the request flow according to our needs. Also, when it comes cost savings, it's best to use them in test and stage ENV and sometimes in Prod as well.


### Prerequisites

Following are required:

```
A k8s cluster(minikube on local system)
Docker(Installed)
Access to docker registry(to push image, so that k8s can pull them)
```

### Setup

A step by step series of examples that tell you how to get a development env running

####To test the working, just execute the following commands.

```
kubectl apply -f app/k8s/deployment.yaml
kubectl apply -f app/k8s/service.yaml
kubectl apply -f nginx/nginx_proxy.yaml
```

#### Make your own changes to the app and build the image.

```
docker build -t <name of your image with registry address>:<tag> .

Example: docker build -t aroraankit/nginx_proxy:v2 .
```

Push the image to your container registry.

```
docker push <name of your image with registry address>:<tag>

Example: docker push aroraankit/nginx_proxy:v2
```

Now make changes in deployment.yaml and nginx_proxy.yaml files image section to the name of your image.


To deploy, execute the following commands.

```
kubectl apply -f app/k8s/deployment.yaml
kubectl apply -f app/k8s/service.yaml
kubectl apply -f nginx/nginx_proxy.yaml
```


### Break down into end to end tests

To check the working, note the LoadBalancer IP and hit the following URL in the browser.

```
http://IP/names
```
