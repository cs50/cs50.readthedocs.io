# Offline

Normally, CS50 IDE requires a constant connection to the internet. This may not fit users with slow or unstable internet connections, or those who want to continue using the IDE offline for any number of reasons. The following instructions walk you through how to download and install the offline version of CS50 IDE. Please note that the new offline IDE may be quite a large download (several GB).


## Installing

CS50 IDE Offline is a containerized app. In order to run it, you need to install a tool called [Docker](https://www.docker.com/). See [Get Docker](https://docs.docker.com/get-docker/) for instructions on how to install Docker for your operating system!


## Creating a new IDE

Once you have installed Docker, you can create a new CS50 IDE by opening up your command prompt or terminal app, and running the following command:

```
$ docker run --detach --env C9_HOSTNAME=0.0.0.0 --env CS50_IDE_TYPE=offline --name ide50 --publish 1337:1337 --publish 8080-8082:8080-8082 --volume path/to/folder:/home/ubuntu/workspace cs50/ide:offline
```

where `path/to/folder` is the path to a folder on your computer where you would like your files and folders inside the IDE to persist, then visit [http://localhost:1337/](http://localhost:1337/) in your web browser to start using your IDE.


## Managing your IDE

### Starting your IDE

If you can't access your CS50 IDE at [http://localhost:1337/](http://localhost:1337/) (e.g., after restarting your computer), your IDE may be stopped. To start it again, open up your command prompt or terminal app and run the following command:

```
docker start ide50
```

### Updating your IDE

Unlike the online version of CS50 IDE, the offline version needs to be manually updated. To update your IDE, you need to pull the latest version the `cs50/ide:offline` image, stop and remove your IDE, then create a new one based on the new image. To do that, open your command prompt or terminal app and run the following command:

```
docker pull cs50/ide:offline
```

then follow the instructions for [Stopping your IDE](#stopping-your-ide), [Removing your IDE](#removing-your-ide), and [Creating a new IDE](#creating-a-new-ide) to create an IDE based on the new image.

### Restarting your IDE

Normally, you shouldn't need to restart your IDE. But if you ever do, open up your command prompt or terminal app and run the following command:

```
docker restart ide50
```

### Stopping your IDE

To stop your IDE, open up your command prompt or terminal app and run the following command:

```
docker stop ide50
```

### Removing your IDE

To remove your IDE (e.g., to create a new one from scratch or when updating), open up your command prompt or terminal app and run:

```
docker rm ide50
```

## Where to Go Next?

Read up on on how to use [CS50 IDE](/ide/online/) itself!
