## BIOLA UNIVERSITY

## EXPLORING THE HOMOPHILY IN TWITTER WITH PYTHON

### Alexander Patton and William Strong

### 26 DECEMBER 2017
________________
## Abstract
In last semester’s Social Networks Research Seminar, a fellow student and I investigated the prevalence of homophilic relationships within Twitter communities. We chose to select the active members of congress, and research the nature of their communication amongst themselves. To our delight, we found 54 members of congress who are active on twitter, and have communicated with one another via direct mentioning within tweets. This paper will investigate the nature of the principle of homophily, including its origins in greek philosophy and early century sociological research, and presence in Twitter at large through a modern case study. There has been significant research into the different aspects of homophily, and recently into homophily in online communities. We felt that utilizing Twitter to research this phenomenon would be a natural extension of the current state of research into the topic. Thus this paper be an analysis of our research in political homophily in Twitter, including our technical challenges, the nature of our data, and our findings. 

## Introduction

Computer science is a wonderfully broad discipline, encompassing not only strictly computational fields, but many associated scientific fields as well. The field of computer science has progressed to the point where technology can be utilized by nearly anyone to make substantive quantitative inferences in many of those related disciplines. My recent research project is a fantastic example of this fact. Homophily is directly related to the structure of social networks, which have deep technological ties. By no means am I a computer genius, however I was able to investigate the presence of homophily in a virtual community because of the technological tools at my disposal. Therefore, I hope to show the closeness of the connection between technology and its application to broader fields through our investigation of homophily in political communities on Twitter.

## Homophily

Homophily is “the principle that a contact between similar people occurs at a higher rate than among dissimilar people”[1]. On face value, this seems obvious, in fact, it has a long history, having potentially originated from the likes of Aristotle, in his Nicomachean Ethics[2]. Aristotle made some of the most obvious statements in the history of philosophy, but like most of his work, this principle is not as simple as it seems. It is one thing to say that people like those who are like them, it is an entirely different and far more complex endeavor to find out in what way, and to what degree this is true. The principle of homophily, therefore, allows us to quantify and solidify the general truth of attraction. The modern principle has its roots in sociology and psychology, and has been studied for the greater part of a century in one form or another.
One extreme benefit of applying technology to sociological studies is the scale of data which online social networks provide. Early studies of homophily in the 20’s and 30’s were only able to procure small data sets from in-person studies[3]. The increasing connectivity of society paved the way for more substantive research, including via large-scale polls, and mail-in surveys in the 70’s and 80’s. Social networks such as Twitter and Facebook provide a massive leap forward in terms of the scale of research. 

Homophily invites analysis into various types of networks. My partner and I chose the social network Twitter since it provided a solid basis for automated data collection, but many researchers have done analysis on familial networks, schools, and even entire countries via surveys. This variety invites several categories of analysis. Lazarsfeld and Merton  indicate that there are two general types of homophily[4]. Firstly, Status Homophily indicates the tendency of people who are in the same social class to associate with one another. Secondly, Value Homophily indicates the tendency of people who share similar values and personal characteristics such as sex, age, race, and religion to associate more frequently with one another. In our project, my partner and I researched homophily according to political party lines. This could fall into either category, but perhaps indicates there is a third overall type of homophily, that of Associative Homophily, or Organizational Homophily. This would indicate that a person who associates with a certain type of organization would more frequently interact with those also associated. Admittedly this is similar to Value Homophily, but I would argue better describes the role of homophily in triadic closure amongst people in shared social circles. In other words, organizational homophily describes the statistical likelihood of two people to connect with one another given their mutual interest in a certain cause or organization such as a political party on Twitter.

Twitter provides an intriguing intersection between computer science and the principle of homophily. For example, a recent study into the distribution of political information utilized Twitter’s large data set to analyze over 2.2 million twitter users with 90 million links in the network. They took politically minded Twitter users, defined as those who followed at least one account associated with a member of the U.S. House during the 2012 election cycle, and then formed a national network and fifty state networks. The network links were defined as one user following another user. Because of the the use of Twitter’s API, discussed in more detail later, they were able to obtain meaningful results which “suggest that … homophily generates a built-in advantage in knowledge for voters belonging to the majority group and … may make it difficult for voters to select the best candidates and to monitor the behavior of politicians once in office”[5]. Studies like this and our own research project indicate a bright future for use of online social networks in sociological analysis.
Project

Twitter provides a plethora of data across all regions of culture and community while at the same time providing a well documented API[6] which allowed us to hand-craft a select data-set to create a network of tweets. Twitter is also home to an inordinate amount of meaningless tweets and fake users. With this in mind, my partner and I chose to select the active members of the House of Representatives as our network vertices. In order to filter out extraneous noise, we limited the connections between the vertices to tweets in which a member of the network mentions another member of the network. Using mentions best mirrors real communication since it necessarily indicates an attempt to communicate directly with another user. Establishing this detailed and curated set of data took significant time, since we attempted to make our framework extensible to more varied data and queries. Our goals for last semester were to create visual representations of the network as a layered model, and as a force directed graph, clustered around metrics such as party, and length of service. Finally, we hoped to establish whether or not politicians tend to exhibit homophily in their communications on twitter.
Data

Twitter provides a thorough API for accessing its data. We used a wrapper written in Python to access the native Twitter RESTful API[7] and then stored the data in MongoDB, a NoSQL database. This allowed us to target specific information without having to pull large amounts of data. Twitter’s data is packaged in JSON (Javascript Object Notation) objects which makes manipulation and storage of the data fairly straightforward[8]. For example, a tweet is presented as a nested JSON dictionary which has several root level attributes which can themselves be dictionaries. This allows for consistent parsing of information, which we utilized to extract all of the mentions to create links between the vertices in our network. Twitter’s API utilizes a rate limitation strategy to prevent certain request from hogging the network bandwidth. They separate requests into 15 minute windows and certain endpoints allow either 15 or 180 requests per window[9]. Thus, we used a caching strategy to temporarily store the tweets we already had into the MongoDB collection and subsequently fill out the collection as the API freed up the endpoint for more requests.

Once we downloaded the tweets of each member of the network, we filtered them for mentions of other network members, and compiled the mentions of each member into a list. In the end, we had a data collection of 54 dictionaries, one for each member, with their name, twitter username, party affiliation, state, and the list of all the users they mentioned as shown below. From this we were able to construct the network of 54 members of congress and their internal communications.
```
{
        User Name:
        Actual Name:
        Years Active:
        District:
        Party:
        State:
        Mentions: [username, username, …]
}
```
## Procedure

This project began as an attempt to modernize the code found in Mining the Social Web[10]. One of the first tasks was to get a browser-based python interpreter called Jupyter Notebook running with introductory interfaces with the Twitter API. This took several weeks, since the codebase from the book was written in Python 2 and therefore severely out of date. For example, it suggested using iPython notebook, but that project has subsequently been folded into the Jupyter project and is now branded as Jupyter Notebook.

The API suggested by Mining the Social Web was unusable out of the box, since it was deprecated several years ago. However, we spent significant time investigating different twitter API wrappers for the Python language, and settled on the aptly-named python-twitter module[11]. This module allowed us to pull any data that was exposed by Twitter’s API and utilize it in our project. 

Our first line of inquiry was into Barack Obama’s tweets. We knew early in the process that we wanted to work with Politician’s accounts since their level of communication was most likely more representative of legitimate language than the majority of tweets. Getting Obama’s tweets opened our eyes to the challenge of Twitter’s rate limits. As my partner created a more extensible framework for obtaining tweets, he had to integrate controls into the software to deal with the fact that Twitter only allows a user to pull up to 3200 tweets of a given user, in addition to caching tweets to get around the timing rate limits. Thus, it was not a simple matter to get our data. In fact, we spent the majority of our time obtaining and curating the data.

Even though we were using the python-twitter module to communicate with twitter, the data which twitter provided was unusable in any graph visualization software. Thus, we had to create a framework that not only interfaced with python-twitter, but parsed all of the data, sometimes megabytes worth of tweet objects, and stored it in a json-like format to be utilized later by our graphing module. Thus, my partner spent a significant amount of time creating the twitter_controller module in our framework. It not only provides the user with an interface into the python-twitter API, but communicated with our other module, the database_controller, to modify the results, and store them into a JSON-like MongoDB specific BSON format to store in our persistent database on an AWS server.

As mentioned above, we needed a way to have the data persist so that we didn’t have to use the prohibitively slow process of pulling data from Twitter each time we wanted to operate on the network. Thus, my partner created a module to access a MongoDB database that we set up on an AWS server. In it, we created a collection which mapped all of our data in the JSON-like format shown above. Thus, we are able to create a graph out of all of the usernames, and their mentions which function as a sort of adjacency list. The other metrics are used for clustering and determining homophily.

The final step that we took before being able to begin researching was to find and learn a software package which allowed us to create and manipulate graphs. In our search we found several candidates, but the Graph-tool[12] package was the most performant and extensible by far. It includes functionality to not only create graphs, but to give them a number of different layouts including radial, force-directed, and nested. Additionally, it provides modules to calculate a number of different metrics about the network such as clustering coefficients, and to do different searches of the graph.

The major difficulty we experienced with Graph-tool was integrating it into our software. It is extremely performant, since it utilizes a C++ framework under the Python interface to do the computational portion of the functions, however this also means that it has very specific compilation and environment requirements. Thus, we spent over 15 hours simply trying to get it to run on our local machines. In the end, we used Docker[13], a software that allows a user to run multiple virtual-machine-like containers on a kernel daemon to run the software. The creator of Graph-tool created a Docker image that had the software’s necessary settings pre-installed. Finally, we had Graph-tool running in a Docker container, linked to our Python integrated development environment as the default interpreter allowing us to write python in our native system and also utilize Graph-tool. 

We created a method which takes a Graph-tool graph structure, and a property of that graph such as party affiliation or location, and investigates the presence of homophily as a “deviation from what a baseline model of random assortment would predict” within the graph[14]. First, it determines the probability of any given node having a given value of the property as either probability 1 (P1) or probability 2 (P2). Then it calculates the average distribution of heterogeneous edges by finding . It then searches it searches every edge in the graph and determines whether or not that edge has a source and target vertices that are the same in terms of the property, and counts the heterogeneous edges. Finally it determines the actual prevalence of heterogeneous connections by finding (heterogeneous edges/total edges).

## Findings

One of the primary points of interest for us during the last semester was whether or not U.S Senators exhibited significant homophily in their interactions on twitter. We felt that if we were able to establish a positive relationship of homophily in their interactions on Twitter, it would indicate that perhaps twitter has some bearing on real life communications among politicians. Therefore, to our delight, we were able to establish that there was significant homophily along party lines. Our findings indicate that on average, 44% of edges should be cross-party edges, and in actuality, only 18% are. Therefore, out of 427 total edges, only 77 were heterogeneous, and 350 were homogeneous. The homophily is visually represented by graph 2 below. 

Additionally we calculated homophily based on the length of service. In order to do this, we took the length of service property, and considered ten years of service to be a cutoff point. In other words, any edge in which a junior congressman, of less than 10 years, and a senior congressman, of 10 or more years, were communicating, we considered to be a heterogeneous edge. Our findings were very interesting. In a very distinct differentiation from the party line homogeneity, this metric indicated no evidence of homogeneity. In fact, the fraction of heterogeneous edges (0.489) was almost identical with the estimated probability of heterogeneous edges (0.49). The visual representation of the graph clustered into junior and senior congressmen can be found in graph 3.

One of the most intriguing things about politician’s communication is that they are largely split into 2 different groups. Republicans and Democrats. It is fairly intuitive that there would be more communication within party bounds than outside of them, however, without being able to visualize it, the significance of that clustering is not readily evident. Graph 2 below shows just how significant the rate of communication between members of the same party really is.
Conclusion

Homophily is prevalent in all forms of communication and human interaction. Noticed by philosophers, studied by sociologists, and exhibited by online social networks, homophily provides the perfect opportunity for computer scientists to bring to bear their technical capabilities to study social phenomenon. My research partner and I followed in the footsteps of Halberstam, Yosh and Knight when we undertook to investigate homophily among politicians on twitter. After curating our data via the Twitter API, we were able to establish the presence of significant homophily in regards to political party, and also confirm a distinct lack of homophily based on seniority within congress. The future is bright for research into homophilic relationships, and as computer scientists we ought to be leading the way.








## Appendix A: Graphs
#### Graph 1:
This graph shows the nested block model of the graph in a radial layout with node size increasing as the number of edges increases.
  
![alt text](images/graph_1)
________________

#### Graph 2:
This graph shows the network clustered by party in a force directed layout
  
![alt text](images/graph_2)
________________

#### Graph 3:
This graph shows the force-directed graph of congressmen clustered on seniority. Green nodes indicate a senior congressman of > 10 years service. Blue nodes indicate a junior congressman of < 10 years service.
  
![alt text](images/graph_3)
________________

#### Graph 4:
This graph shows the minimum spanning tree of the graph. Nodes are colored according to party.
  
![alt text](images/graph_4)
________________


## References
"API reference index - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/api-reference-index. 
Aristotle. "Chapter 8." In Nicomachean Ethics, edited by Terence Irwin. Indianapolis, Indiana: Hackett, 1999.
Easley, David, and Jon Kleinberg. Networks, crowds, and markets reasoning about a highly connected world. Cambridge: Cambridge University Press, 2016.
"Docker Documentation." Docker Documentation. January 09, 2018. Accessed January 10, 2018. https://docs.docker.com/.
Lazarsfeld PF, Merton RK. 1954. Friendship as a social process: a substantive and methodological analysis. In Freedom and Control in Modern Society, ed. M Berger, pp. 18–66. New York: Van Nostrand
Halberstam, Yosh and Knight, (2016), Homophily, group size, and the diffusion of political information in social networks: Evidence from Twitter, Journal of Public Economics, 143, issue C, p. 73-88, http://individual.utoronto.ca/halberstam/homophily_twitter.pdf
McPherson, Miller, Lynn Smith-Lovin, and James M. Cook. "BIRDS OF A FEATHER: Homophily in Social Networks." Annual Review Of Sociology 27, (August 2001): 415. Business Source Premier, EBSCOhost (accessed January 10, 2018). 
Peixoto, Tiago P. "graph-tool 2.26 documentation." Accessed January 10, 2018. https://graph-tool.skewed.de/static/doc/index.html.
"Python-twitter documentation." Accessed January 10, 2018. https://python-twitter.readthedocs.io/en/latest/.
Russell, Matthew A. Mining the social web. Sebastopol: OReilly Media, Inc, USA, 2013.
"Tweet object - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object. 
________________
[1] McPherson, Miller, Lynn Smith-Lovin, and James M. Cook. "BIRDS OF A FEATHER: Homophily in Social Networks." Annual Review Of Sociology 27, (August 2001): 415. Business Source Premier, EBSCOhost (accessed January 10, 2018).
[2] Aristotle. "Chapter 8." In Nicomachean Ethics, edited by Terence Irwin. Indianapolis, Indiana: Hackett, 1999.
[3] McPherson, Miller, Smith-Lovin, and Cook. “BIRDS OF A FEATHER”
[4] Lazarsfeld PF, Merton RK. 1954. Friendship as a social process: a substantive and methodological analysis. In Freedom and Control in Modern Society, ed. M Berger, pp. 18–66. New York: Van Nostrand
[5] Halberstam, Yosh and Knight, Brian, (2016), Homophily, group size, and the diffusion of political information in social networks: Evidence from Twitter, Journal of Public Economics, 143, issue C, p. 73-88, http://individual.utoronto.ca/halberstam/homophily_twitter.pdf
[6] "API reference index - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/api-reference-index.
[7] "API reference index - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/api-reference-index.
[8] "Tweet object - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.
[9] "Rate Limiting - Twitter Developers." Twitter. Accessed January 10, 2018. https://developer.twitter.com/en/docs/basics/rate-limiting.
[10] Russell, Matthew A. Mining the social web. Sebastopol: OReilly Media, Inc, USA, 2013.
[11] "Python-twitter documentation." Accessed January 10, 2018. https://python-twitter.readthedocs.io/en/latest/.
[12] Peixoto, Tiago P. "graph-tool 2.26 documentation." Accessed January 10, 2018. https://graph-tool.skewed.de/static/doc/index.html.
[13] "Docker Documentation." Docker Documentation. January 09, 2018. Accessed January 10, 2018. https://docs.docker.com/.

[14] McPherson, Miller, Smith-Lovin, and Cook. “BIRDS OF A FEATHER”
