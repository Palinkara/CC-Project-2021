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

- **Users:** People using the application to organise their daily life and events
- **(Planning) organisation:** The party who needs the analysed data given by the users to plan successful events
- **Calendar:** The element containing all dates and events noted by the users
- **Analyser:** The WordVector-based tool used to evaluate the events given by the users

## Milestones & Documentation of them
- [Hito#0 - Milestone#0](Hito%230/Hito0.md)
