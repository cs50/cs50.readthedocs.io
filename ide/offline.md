# Offline

Normally, CS50 IDE requires a constant connection to the internet. This may not fit users with slow or unstable internet connections, or those who want to continue using the IDE offline for any number of reasons. The following instructions walk you through how to download and install the offline version of CS50 IDE. Please note that the new offline IDE may be quite a large download (several GB).


## Installing

CS50 IDE Offline is a containerized app. In order to run it, you need to install a tool called [Docker](https://www.docker.com/). See [Get Docker](https://docs.docker.com/get-docker/) for instructions on how to install Docker for your operating system!


### `ide50`

Instead of using Docker commands to manage your IDE, you may use `ide50`, a command-line script that facilitates using CS50 IDE Offline. To install `ide50`, open up your command prompt or terminal app and run the following command:

```
pip3 install ide50
```

Run `ide50 -h` to verify that the installation was successful and see usage information.

You may need to install [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) first, if not already installed on your system.


## Starting Your IDE

Once you have installed Docker and `ide50`, you can start your IDE by opening up your command prompt or terminal app, and running the following command:

```
ide50 start
```

## Stopping your IDE

To stop your IDE, open up your command prompt or terminal app and run the following command:

```
ide50 stop
```

## Updating Your IDE

Unlike the online version of CS50 IDE, the offline version needs to be manually updated. To update your IDE, open up your command prompt or terminal app and run:

```
ide50 update
```

then follow the instructions for [Stopping Your IDE](#stopping-your-ide) and [Starting Your IDE](#starting-your-ide) to start an IDE based on the updated image.


## Checking the Status of Your IDE

To check whether or not your IDE is running, open up your command prompt or terminal app and run:

```
ide50 status
```

## Where to Go Next?

Read up on on how to use [CS50 IDE](/ide/online/) itself!
