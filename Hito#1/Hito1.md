# Hito 1 - Milestone 1
This document is employed by the student to explain and describe the specific steps the student was taking to obtain the result presented in the integrated version.

## Paso 1 - Step 1
To be able to design the following milestones and the with them associated issues, the student had to understand the different types of users using the application in the future and their goals and pain points.

The result is the following:

**Two different user types** are to be expected:

- **"The User"**: The person who will use Planify to add their own events or search for similar projects. Their gain out of this application is the easy communication with their colleagues for private event sharing or inviting. (e.g. Lena wants to hold a tea party and puts it online for colleagues with similar interests to see and declare their interest.)
- **"The Event planner"**: In this case we have the person (or the people) "on the other side" of the application. While The User will use the application to share private events, The Event planner is able to analyze (through either WordVectors or a Neural Network) the information shared and to evaluate which types of events are the most popular with their organisation's members. Like this they can use the information gained to plan own successful events (which will find place during the free time of the organisation's members). (e.g. Carl wants to plan a public viewing for a football game, but doesn't know whether any of the organisation's members would participate in this event.)

## Paso 2 - Step 2

Now after having defined the two user groups for the application, the student was able to design user stories - stories that are realistic scenarios to be encountered by a user.

Those mainly consist of the following structure:
"As a **(user group/role)**, I need to **(task the user wants to accomplish in a standard scenario, includes context)**, to **(goal user wants to reach).**"

All user stories designed by the student are following this format.

In addition to naming them, the student will also provide a short description about where the task comes from, which scope the student expects for it to have and why it is important enough to be mentioned with the priority it is (priority matches the number of the story).

### US 1: As an Event planner, I need to be able to see how many events of a specific type are planned, to organize events my organization's members would be interested in.

This task describes the core function of the application, the function making this application of worth for the organization to use in the future. In this case the user consists of the **Event planner** (see Paso 1). 

It's the most prioritized user story as the application depends on it:

If the Event planner isn't able to see which event types are the most popular with the organization's members, he could just as well use a simple (online) calendar for his organization, as the value would be roughly the same.

It's also the user story with the biggest scope - depending on how the evaluation process can be implemented, it requires invested work concerning WordVectors or Neural Networks by the student.

### US 2: As an Event planner, I need to get a list of all the events and the types they were listed as, to have examples for each event type and to know the specific events already organized from each event type. 

This task is a continuation of the core function and it's concerning the **Event planner** who now not only needs the numbers of the specific event types planned through which they know about the event type's popularity, but also which events were considered as which event type.
While for example "Watching a movie" as an example for the event type "Film/Series" won't help the Event planner, an event like "Golf" being mentioned ten out of fifteen times in the category "Sports" might be a good indicator for the popularity of this specific sport.

That means, that the original functionality from US 1 will be expanded to include this.

The scope is esteemated to be low in comparison, as most of the code written for US 1 could probably be reused.

Although this is just an extension of US 1, it is still categorized as priority two to make the by the application proposed unique selling point complete. 

Based on this more "normal" functions can be added for The User.

### US 3: As an organisation's member (see The User), I need to be able to add my own events to make them visible to other members (Users).

At this point the user stories switch to the perspective of The User.

After having implemented - or at least designed - the functions concerning the unique selling point, other more known functionalities can and should be added.
These primarily include the functions without which the unique selling point wouldn't be applicable - if nobody is able to add events, the Event planners won't be able to plan. With or without the application.

So now the next goal is to make the application useful from the User's side and make it attractive to use.

These functionality requires a specific design and an analysis in function, for which reason it's still impossible to estimate the specific amount of work needed to fulfill the tasks implicated in the user story.

The scope should be estimated in more detail once the other tasks derived from the first two user stories are fulfilled.

### US 4: As an organisation's member (see The User)/Event planner (both apply!), I need to see when other events are planned (and possibly who attends them).

This is a function interesting for both - The User and The Event planner. For the user this function is useful because based on that they can choose when and which events to attend. 

It's useful for the Event planner as they are able to see when which event takes place and plan accordingly (e.g., for the planned event not to clash with other events).

This functionality is just a important as US 3 and also requires a lot of design specifications. 
The order of these two user stories being mentioned doesn't influence their priority that much, as it's comparable to the chicken-egg-problem.

Does it make more sense to give the user the chance to add events or to see them without giving them any chances to add?

Certainly both are important functions with a prioritarization of 3 to 4.