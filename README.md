# Intent
This is a simple Flask application running on Elastic Beanstalk and backed by MongoDB. The site mocks an oAuth request to the DroneDeploy API (which doesn't exist) and 'fetches' the auth'd user's flight history and fleet data. Based on this data, it builds two pages:

1. **The Analytics Page:** This page renders graphs and high level stats based on the user's previous flight data queried from the fake DroneDeploy API.
2. **The 'Your Fleet' Page:** This page renders the user's fleet (grouped by Drone Make/Model) and lists suggestions to improve performance based on global data from all DroneDeploy users.

This site was built for entertainment purposes only and is not in any way associated with the DroneDeploy service.

The production site can be found at: **[http://www.ddanalytics.com/](http://www.ddanalytics.com/)**



# Project Scope
Due to time constraints, this project is limited in scope. I essentially wanted to see how quickly I could pick up Flask, model and develop a functional site, and deploy it on AWS. That said, here are some of the concessions I have made along the way:

###Data:
Obviously, DroneDeploy doesn't have a publicly available API. In this case, I [modeled](https://github.com/cooncesean/ddanalytics/blob/master/models.py) what I assumed to be reasonable documents based on what I know about DroneDeploy as well as what I needed to render to users on this site.

The models are fairly straightforward:

* **User:** This document contains all user fields as well as methods to fetch flight and drone data based on each individual user. If this were real we would be storing oauth tokens, etc in this document.
* **Drone:** This document contains drone fields (make, model, battery, motor etc.) as well as a ReferenceField to the User that owns it.
* **FlightHistory**: This document works as a 'flight log' for both users and drones. It is used to build out a number of statistics/graphs for the User at runtime.

For the sake of the example, there is only one user in the system `Mock User`. This user has a number of drones and flights generated for them via the `ddanalytics.utils.generate_dev_data()` command - which is typically called from the `bootstrap` management command. Regardless of how the UI works, all authenticated users still only view this default user's statistics.

###Mocked oAuth:
In the interest of time, I have decided against implementing full oAuth integration into this sample site. All auth, redirects, tokens, etc. are currently mocked. In the meantime, I'll peruse the [http://pythonhosted.org/Flask-OAuth/](http://pythonhosted.org/Flask-OAuth/) extension for reference.
