# FetchMuniTimes
Deployment package for an AWS Lamba returning the next times at a station tracked by 511.org.

This Python Lambda can be mapped to an AWS API Gateway GET Resource with 3 URL parameters:
* uuid: the UUID of a Transit Tracker created at https://511.org/transit/tracker/overview
* min: the minimum time to display (in minutes, default is 0)
* max: the maximum time to display (in minutes, default is 99)
