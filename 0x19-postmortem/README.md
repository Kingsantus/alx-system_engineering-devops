# Postmortem

## Task
the task of this project is to know how to write a bug
so this project indicated that as a software developer you will expirence bug in different places
it your job to write about it and publish it to the company

the reason for the writing is 
1. To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
2. And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

the format includes

1. Issue Summary (that is often what executives will read) must contain:
duration of the outage with start and end times (including timezone)
what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
2. what was the root cause
Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

3. when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
4. how the incident was resolved
Root cause and resolution must contain:

explain in detail what was causing the issue
explain in detail how the issue was fixed
Corrective and preventative measures must contain:

5. what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
