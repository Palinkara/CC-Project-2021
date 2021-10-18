# Planify

## What is the goal of this project?
In the module "Cloud Computing" students are supposed to learn how to cloud compute by working on their own project which will
- provide business logic,
- be hosted in a cloud,
- and process data in a meaningful way (search options are not enough!).

The name of the project is Planify and its purpose is explained in the following description (both - in a nutshell and in more detail).

## Project Description in a nutshell...

The goal of this specific project is to create an application for organisations which plan to provide their members with events, but have no idea which events might be popular.

To do this an application will be created in which the members are able to note down their private events and parties. By doing this the organisation is later able to evaluate the noted events by using a Wordvector-trained system and therefore to see which eventtypes (types! "Movies/Series" is a type - "Captain America" is not. Same for "Music" and "Panic! At the disco-concert".) are popular with their members and plan internal events accordingly.

Based on that events can be organised which will leave all parties involved satisfied.

## ... or in more detail

Let's be honest - we all know this problem.

Whether we're talking about our local (or international, for that matter) friendgroup or the organisation we're active in - we all know the situation considering event planning. Especially if you're in the planning party.

If you're not - let me explain to you. 

As a member of the planning party, there are lots of things you have to keep in check:
When is Mr Smith free to attend to event? Which food is Mrs Christie allergic to? Was it Mr Doyle who announced he would never visit a reading session?

Just to name a few of them.

And sadly, even *if* everything is perfectly planned and everybody has time and the food is right, it doesn't mean there will be lots of people present.
Maybe out of fifty people invited, five will arrive.

If you later ask for the reason, the answer, most of the time is rather similar: "I didn't have enough time" or "I'm sorry but (insert activity) was never something I enjoyed".

To be able to go against this rather annoying situation, I want to present you **Planify** - an app hosted in the cloud which could do exactly what you need it to.
With its help, you're perfectly able to see which weeks are rather busy, when which person is available and - which events people are generally interested in.

The application is structured as follows:

First of all - every member of an organisation is granted access on this app.
Every party is simultaneously able to introduce their plans in a calender to make them available to other parties which might be interested.
E.g. Mrs Christie is hosting a small get-together and is open for people from her organisation taking part in it. So she puts it in the application making it thus visible for all.
What does happen now?

Two things:

1. Other members in the organisation are able to see her notice and contact her to take part in her get-together, which will leave both - the organisation members **and** Mrs Christie satisified and
2. the planning committee is able to use the information introduced to add it to their database, based on which the WordVector-based application allows to evaluate trends in (private) event planning introduced into the organisation.

Of course all of this will happen with permission of the users themselves - the organisation should never employ this technique without getting the permission of all parties involved.

After having analysed the trends in event planning, the organisation is now able to use the information gained for their own planning:

They know who is free at which time and which events are generally favoured by the organisation members thus increasing the probability of a high satisfaction level with a future event.

Make your members happy - plan successfull events.
Only with Planify.

Thank you for your attention.

## Elements of this projects

There are several elements the application will be based on. To name the most the important ones:

- **The User:** People using the application to organise their daily life and events
- **The Event Planner:** The party who needs the analysed data given by the users to plan successful events
- **Calendar:** The element containing all dates and events noted by the users
- **Analyser:** The WordVector-based or Neural Network-based tool used to evaluate the events given by the users

The architecture of this project will be **event-based architecture** as a continuous updating/processing is not needed and only happends after certain events (e.g. "Event is added by User" or "Event Planner started evaluating process").
The events are yet to be defined.

## Milestones and their Documentation

As the user stories and milestones were planned and designed in complete unison, most of them coincide with each other.
Nonetheless, the associated user story is always mentioned with the specific milestone.

The project concerning the milestones is structured as following:

### Hito#0 - Milestone#0

[Hito#0 - Milestone#0](Hito%230/Hito0.md)
The student's Github account is prepared to starting a project.
Additionally, the student now knows all the basic functionalities of Github and can use them according to formal conventions provided.
A general project idea (including business logic and the potential to be deployed in the cloud) is presented and described.

### Hito#1 - Miletone#1 - User Stories, Issues & Milestones

[Link to Milestone 1](https://github.com/Palinkara/Planify/milestone/1)

[Hito#1 - Milestone#1](Hito%231/Hito1.md)

After having everything prepared and the project concept validated, the student is now able to design User Stories and based on that, Issues to tackle to implement the application.

Apart from that, the milestones for the student to follow were designed and also the first classes/files needed declared and commented (not yet implemented!).

The latter can be found in combination with the associated issue at: 

[[I 0] - Finish documentation including US, Issues & Milestones](https://github.com/Palinkara/Planify/issues/16)

[[I 1] - Create (and comment) the classes expected to be needed](https://github.com/Palinkara/Planify/issues/5)


The User Story started at this point is:

[[US 1] As an Event planner, I need to be able to see how many events of a specific type are planned, to organize events my organization's members would be interested in.](https://github.com/Palinkara/Planify/issues/1)

### Hito#2 - Milestone#2 - Core functionality & Neural Network

[Link to Milestone 2](https://github.com/Palinkara/Planify/milestone/2)

After having the project structured in User Stories, corresponding tasks and milestones, the second milestone is employed to create a MVP or in this case - to implement the core functions of the application. 

Those consist in the design of a general process when employed by an Event planner, the creation of the classification-algorithm (probably Neural Network based), its training and its testing and the design of general easy-to-read data representation.

After this milestone the Event planner should be able to evaluate how many events of a certain type are planned and ideally name the number to the planner.

Issues associated with this milestone are:

[[I 1] - Create (and comment) the classes expected to be needed](https://github.com/Palinkara/Planify/issues/5)

[[I 2] Create a mock-up to understand the specific process an Event planner will go through](https://github.com/Palinkara/Planify/issues/6)

[[I 3] Create a list of event types and the associated (specific) events (future training)](https://github.com/Palinkara/Planify/issues/7)

[[I 4] Build a Neural Network for future training purposes](https://github.com/Palinkara/Planify/issues/8)

[[I 5] Design an easy to read representation for the Event planner](https://github.com/Palinkara/Planify/issues/9)


The User Story associated with this milestone is:

[[US 1] As an Event planner, I need to be able to see how many events of a specific type are planned, to organize events my organization's members would be interested in.](https://github.com/Palinkara/Planify/issues/1)

### Hito#3 - Milestone#3 - Extension Core functionality & USP

[Link to Milestone 3](https://github.com/Palinkara/Planify/milestone/3)

Similar to the second milestone, my third milestone will focus on the extension of the core functionality. This has to be done, as the core functionality - the analysis of different events, the sort into different event types and the later display of how many events of a certain event type were planned - constitutes the unique selling point (USP) of this application.

In this case, the application is extended by further functionalities, like the display of which events were sorted under which event type.

Issues solved in this milestone are:

[[I 6] Add the additional data to the previous model](https://github.com/Palinkara/Planify/issues/10)

[[I 7] Implement an easy to read representation based an [I 5]](https://github.com/Palinkara/Planify/issues/11)


The User Story associated with this milestone is:

[[US 2] As an Event planner, I need to get a list of all the events and the types they were listed as, to have examples for each event type and to know the specific events already organized from each event type.](https://github.com/Palinkara/Planify/issues/2)

### Hito#4 - Milestone#4 - User side & Event add

[Link to Milestone 4](https://github.com/Palinkara/Planify/milestone/4)

After having implemented the core functionalities constituing the USP, the application will be looked at from an User's (see "The User", not to confuse with "The Event planner") point of view and extended by functions that might seem "normal" (like for example "adding events"), but nonetheless are an important part of the final application.

Those primarily consist of giving the User the possibility to add events. 
(Why this is chosen before the "giving the User the chance to see events"-functionality, is explained in the document concerning the User Stories (see Hito#1 - Milestone#1)).

Issues resolved at this stage are:

[[I 8] Create a mock-up to understand the specific process a User will go through](https://github.com/Palinkara/Planify/issues/12)

[[I 9] Create a standard format a user is allowed to add data](https://github.com/Palinkara/Planify/issues/13)

[[I 10] Research possible methods to represent events added by the user](https://github.com/Palinkara/Planify/issues/14)


The User Story associated with this milestone is:

[[US 3] As an organisation's member (see The User), I need to be able to add my own events to make them visible to other members (Users). ](https://github.com/Palinkara/Planify/issues/3)

### Hito#5 - Milestone#5 - User & Event planner extension & Events watch

[Link to Milestone 5](https://github.com/Palinkara/Planify/milestone/5)

After having implemented the one side of the application enabling the User to post events, it now is important to make the other side possible: The enable all users (The User and The Event planner) to see the events already added.

Issues associated with this milestone are:

[[I 11] Create a mock-up to combine the different views of User and Event planner (if possible!)](https://github.com/Palinkara/Planify/issues/15)


The User Story associated with this milestone is:

[[US 4] As an organisation's member (see The User)/Event planner (both apply!), I need to see when other events are planned (and possibly who attends them). ](https://github.com/Palinkara/Planify/issues/4)

### Hito#6 - Milestone#6

[Link to Milestone 6](https://github.com/Palinkara/Planify/milestone/6)

Cloud deployment. If everything works out, the application should now be ready to be deployed in the cloud.