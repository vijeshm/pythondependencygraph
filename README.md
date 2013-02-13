**usage:** python depgraph.py module_name
**output:** a .graphml file

##The Python Module Network

![networkx module](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/networkx_modules.png?raw=true)

![dependencies between commonly used modules](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/entire_modules.png?raw=true)

![nltk module](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/nltk.png?raw=true)

![numpy module](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/numpy.png?raw=true)

![simplecv module](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/simplecv.png?raw=true)

![urllib2 module](https://github.com/vijeshm/pythondependencygraph/blob/master/sample/urllib2.png?raw=true)

Importing a module in Python! Hmmm.. one of the easiest tasks around, eh? Not so fast, whats going on back there? Is the module importing any other module in turn? Well, sometimes yeah. This behavior propagates through a chain of imports. And whats the best way to model the scenario? Thats right, you guessed it! A Graph. A directed one to be more precise.

Well, what if I somehow magically gave you the import graph to play with? What'll you do with it?
* For starters, you could use it to find the number of modules that a particular module is dependent on. Its just the outdegree of the module node.
* Next, you could find how two modules are related (or even find out if they are even related at all). Thats easy, just find out a path from source to destination. Simple, isnt it? 
* Ok, lets get a bit more serious. Wouldnt you want to find out the hotshots of the modules? No? Oh cmon. Its simple you see, the node with the highest number of paths ending with that node is numero uno hotshot, and the pattern follows. 
* Now, more serious stuff coming up. Buckle up! Ever wondered what the most "important" import would be? Technically speaking, this would be the edge with the highest betweenness centrality.

Given a dependency graph, you'd be able to deduce all these cool stuff just with the right tools and a few mouse clicks. So, what are you waiting for? start generating those graphs.
