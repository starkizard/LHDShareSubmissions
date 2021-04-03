# How to manage & view resouces that are acquired by your Linode

Prerequisite: You know how to set up a Linode , and it is running

##  Checking Disk Usage
![image](https://user-images.githubusercontent.com/42800934/113471384-8946bc00-9479-11eb-83e3-38b60e366952.png)
You can see the disk usage of all the volumes you've mounted through this command (df -h)

The most important one is the one with '/' also known as root filesystem or rootfs. Here I can see I've used 237G out of 358G available and have 121G available.
This can be handy if you see your server suffering from memory issues

There's a tool which can help us take a closer look into what is occupying space : ncdu (not installed by default)

Command = ``` sudo ncdu -x / ``` 
-x flag tells to just scan the local filesystem and ignore the rest , and / is the target directory, from where it starts to scan (also has subdirectories)
![image](https://user-images.githubusercontent.com/42800934/113471558-d2e3d680-947a-11eb-9be3-d6958788b5bf.png)
![image](https://user-images.githubusercontent.com/42800934/113471590-fe66c100-947a-11eb-82f5-05a46cc39357.png)
Now You can use your arrow and enter keys to navigate through your file system and can see in the brackets how much disk is that thing occupying.

## Checking System Memory
Command = ``` free -m ```
![image](https://user-images.githubusercontent.com/42800934/113471637-48e83d80-947b-11eb-88ab-f8e372efd23a.png)
Here, you can see I have about 1.7 Gigs of Memory left available

## Checking CPU usage
An Important command is : ``` uptime ```
![image](https://user-images.githubusercontent.com/42800934/113471680-a086a900-947b-11eb-9402-ee9f383cc96f.png)
Tells you how long the server has been up, and tells you the load average. There are 3 numbers denoting Load averages at 1 minute, 5 minute and 15 minute respectively

Thus in my case, the load avg 1 min ago was 0.52, 5 min ago was 0.58 and 15 min ago was 0.59.

If the load avg == the number of cores, then the server is being 100% utilized. 


Another useful tool is : ``` htop ```
![image](https://user-images.githubusercontent.com/42800934/113471765-44705480-947c-11eb-9eb3-57546bdb91f6.png)
We can see the core -- by core usage of CPU, Memory Usage And all the processes that are running. 

