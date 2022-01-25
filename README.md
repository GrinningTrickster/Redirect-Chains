# Redirect-Chains
Identifies redirects and redirect chains to produce a simple report that can be used for analysis/visualisation. 
<br>
<br>
## **Redirect Chain Report**
<br>
The redirect chain report is able to provide a simple excel report to identify redirects and redirect chains.
<br><br>
The only addition required to this script is a text file in the folder of the project with a list of URLs that are to be checked.
<br><br>
In the instance of a redirect chain, so as to produce a more streamline output that can be used for visualisation purposes, the results will include the number of redirects, the final redirect in the chain and it’s status, as well as the second redirect in the chain and its status. This should present with enough information for larger scale projects to identify redirect issues and recurring patterns.
<br><br>
In the event of a redirect loop or an extremely long chain, the script will trace up to the tenth redirect. Beyond this point, the result will output 11 – and will need a manual investigation to determine if it is an infinite loop. 

  

