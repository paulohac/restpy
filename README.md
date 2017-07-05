# Web API for Prezis

* [Guidelines](#guidelines)
* [Provisioning](#provisioning)
* [Deployment](#deployment)
* [Conclusion](#conclusion)

## Guidelines

This project aims to demonstrate how to build a simple API that can: List all Prezis;
Get a single Prezi by id;
Do a Full-text search for a Prezi by title ordering by creation date

The components and services that are part of this project are listed below:

* Vagrant
* Virtualbox
 * 1 VM Ubuntu/xenial64 (Docker)

* Docker Components
  * Docker Engine
  * Docker-compose

* python3
* Flask
* Swagger UI

## Provisioning

The VM provisioning is handled by Vagrant. In order to bring them to an operational state just clone this repo and run:

`$ vagrant up --provision`

The whole operation will take some time, especially if you don't have the box described in the Vagrantfile.

Using the `:BASH` provider all the necessary packages will be installed (Docker engine + docker-compose )
After the completion of the process you can check the status of the machines running:

`$ vagrant status`

The status of the machines must be `Running`. If not, you can restart the process and check what went wrong. Remember to run `$ vagrant halt` to turn off the running instance before.

The first step after have successfully provisioned the VM with Docker components is to start docker-compose. This process is also automatic and will download postgresql most recent docker image and build another image using the Dockerfile.

The Dockerfile uses Python3 official image wich is edited to fit the app, adding the code base, the list of requirements and the JSON file we will use as seed.

Since docker-compose still cannot effectively make a container to wait for another to be ready a script wait.sh is added in order to make the api container wait for the potgres container to be listening.

## Deployment

The api was deployed in AMAZON AWS and it can be accessed at:
http://54.71.96.100:5000/apidocs

You will be prompt with Swagger UI, a more interactive way to present the methods we are able to call:

GET /prezi:
Returns a list of Prezi's ( pagination is used in order to avoid long lists, default of 10 results/page)

GET /prezi/{prezi_id}
Get a single Prezi from database

## Conclusion

Architecture decisions will usually involve factors like time, the level of productivity of your team, the cost that will be paid for cloud providers in a long term, Scalability, Redundancy, and Security.
Today most of the cloud providers let us decide how is gonna be our level of support, where we can choose to purchase most of all those factors and decide to pay as we need.
When it comes to scalability in cloud-based services we need to start by designing an infrastructure that can afford to scale.

By choosing stateless services we are able to use as many instances as we need since RESTful services allow us to do so by the fact that any service instance can respond to any request.
Then we can configure the elasticity of our services allowing to increase when the load is high and decrease when is not needed by monitoring the response time of those services together with resources like CPU, Virtual memory, physical memory ...

Also, another important point of our infrastructure is to have event-driven states which can make communication asynchronous where the consumers will process events as they can. An excessive load can make your API slow down as the requests piles up, but it won't bring your service down.

There are many ways to build an orchestration layer for managing the life-cycle of containerized applications, today we have Kubernetes, Docker Swarm, or Mesos. Recently Amazon is also offering an orchestration service called  EC2 Container Service and it serves auto scaling of containers. which allows us to scale horizontally across ECS Instances to handle more workload in parallel.

One of the great advantages of centralizing the scheduling operations of orchestration using a central API is that the Docker API is not exposed in any moment. Consequently, only pre-defined events are allowed. This improves the security of the management of the containers avoiding the attacks due to the minimal exposure.

The implementation of an Orchestration can also be achieved by using configurations management tools such as Saltstack API. Although today Cloud providers offer us with detailed insight into the utilization of resources and complete toolkits for setting up effective event-driven Auto Scaling services.
