**EXCALIBUR PROJECT NEPTUNE KICK-OFF MEETING**

Wayne Arter on behalf of UKAEA

(Produce a pdf from this markdown format file using pandoc, on Linux:
pandoc -o intro_wa.pdf intro_wa.md )

# Slide 0.
ExCALIBUR slide format adapted for UKAEA usage.

# Slide 1.
I have adopted the convention of UK university lectures that a nominal 9.00am
meeting has its first presentation starting at 9.05am.
Talks are given the titles used on the corresponding call document.
Times allow approximately 5 minutes for discussion and introduction of people
likely to work on the Excalibur project Neptune.

# Slide 2.
This is what I'm proposing to run through quickly with emphasis on the next 6-9 months.

# Slide 3. 
First, let me thank you all for attending, given present circumstances of Lockdown.
Especial thanks to those who had to face two meetings with me in under a fortnight.
(I trust you appreciate that was necessary so this meeting could be transacted within
half-a-day of everyone's time.)
This group includes the bidders for work on Excalibur-Neptune. 
I'm conscious that we haven't really thanked you all for your efforts.
As the preparer of many proposals, I have to say that personally I was impressed by
your ability to assimilate the information thrown at you into constructive,
conforming proposals in a short time given your other often heavy teaching commitments.
Further that I have been confirmed in this opinion by close colleagues and by
our Met Office liaison.

# Slide 4. 
All the presenters, having prepared bids for Excalibur-Neptune within the last
3 months, will be familiar with the aims of the project, so we don't
propose to repeat that information, except as background in this slide.
Anyone else attending who is interested in
such material is recommended to consult the Neptune Science Plan
https://www.metoffice.gov.uk/binaries/content/assets/metofficegovuk/pdf/research/spf/ukaea-excalibur-fms-scienceplan.pdf
and other references to the national Excalibur project available from the web-page
https://www.metoffice.gov.uk/research/approach/collaboration/spf/excalibur

We hope that you will be more
interested to engage with the technical aspects of the project. For various reasons,
not just the Covid pandemic, we are about 6 months behind where we should like to be,
so we need to make useful things happen, and happen quickly. Hence I want this meeting
to concentrate on the next 6-9 months of activity, where we urgently need to steer and
to de-risk the project.


# Slide 5. 
First though I need to run through some admin. Hopefully you have been made aware that
with exception of the Oxford submission, redacted versions of all the winning bids have
been posted in the repo
https://github.com/ExCALIBUR-NEPTUNE/Documents
subdirectory bid_documents

Evidently the latest lockdown is placing a big strain on many people involved
in today's meeting and they are wondering what variations might be permitted
regarding date and nature of deliverables in particular. The Met Office informs
us that they are currently awaiting guidance from BEIS, which will flow down to
UKAEA as the manager of project Neptune.

In any event, it has been agreed with Met Office that UKAEA may seek to minimise
reporting in the current FY ending March 2021 by accepting as Quarterly Report
deliverables for payment,
slide presentations from the workshop meeting proposed for mid-March. (Ultimately
the material will of course have to be written up as part of the technical
reporting process.)
For financial reports at year-end the following details of work performed are required:

- What has been delivered to date 
- What has been invoiced 
- What is going to be invoiced 
- What is being carried over (if anything)

This information  might be included with the slides presented at the mid-March
meeting, perhaps in the "notes" section of a powerpoint, but anyway arranged so that
it could be easily redacted.

UKAEA asks that efforts be made to attend fortnightly online meetings of the community at
least in this initial phase. It is hoped that sufficient motivation will be provided by:

- Responses at alternate ones could form the basis of monthly progress reports.
- Each gathering could be accompanied by one presentation of length between 20 and 50 minutes,
selected using the criteria of interest, timeliness and Neptune relevance.

There is a canonical slide presentation format available for ExCALIBUR work (of which the
current slide set is an example) which presenters may like to adapt to conform their
own institution's branding.

# Slide 6.
UKAEA has produced a graphical representation of the interactions between the various
tasks, which will be made available as a .graphml format file  NEPTUNE_full.graphml.
Unfortunately the resulting diagram is too detailed to display clearly, but this slide gives an 
indication as to what has been produced (as .png file using the yEd software).

# Slide 7.
This is a reminder that not all calls were equal. The main external responsibility for delivering
software resides with the winner (York) of Call T/NA083/20 - call numbers abbreviated to
2 digits 83 in this example, who is expected to incorporate the spectral element
software of the winner of Call 78 (Exeter, with the spectral/hp element package).
The third of the longer calls (Call 84) was to develop a reduced dimensionality (5-D instead
of 6-D time dependent model) gyro-averaged model to account for edge plasma behaviour.
Each of these offered enough resource to fund a post-doc and bidders were more heavily
rewarded for aligning their work with relevant elements of the science plan.

The remaining calls were intended principally to establish state-of-the-art and
Exascale-relevance in specific areas considered relevant to the first years
of the project, namely

- particles (79)
- UQ (80)
- MOR (81)
- Preconditioning (84)
- DSL/code generation (86)

in order that the software not date too quickly for a 30 year lifespan.

# Slide 8.
For the longer calls 78 and 83, the near-term aim is to de-risk the project by
establishing the applicability of the spectral/hp method to problems relevant
to tokamak edge physics. The three problems sketched on the slide, which emerge from
equation sets listed in FMS/021 have not previously been attempted by high order
elements. The first is in the very essence of the problem, where interaction with
neutrals may create density sources and momentum and energy sinks constituting the
dominant terms in the conservation relations for a fluid model of plasma. 
Secondly only when comparatively low density plasma flows into a solid surface
are found sonic flows of fluid into a surface produced using a CAD system.
Moreover, for better power handling critical surfaces are designed so that
the flow incidence is close to grazing, typically around 2 degrees, whereas 9.5
degrees was the smallest angle I found able to present easily. (Rolf Heuer's DEMO
reactor Gate 2 Review identified plasma exhaust and first wall protection strategy within the
first four critical issues to be addressed.)

Lastly, from the Equations document
FMS/021 issue dated 30/6/20, Eq.(20) gives by inspection of the leading numerical
coefficient, a ratio x of order 100 000 for electrons, which translates into a
difference in scale lengths parallel and perpendicular to the magnetic field of
the same magnitude, since the corresponding diffusion coefficients are in the ratio x-squared.
Even at Exascale, the factor 100 000 in mesh-size to be lost by not accounting for
this anisotropy is hard to tolerate.  Moreover, because the field-lines
lie on toroidally axisymmetric surfaces like those sketched at right, which
they wrap around helically with a varying pitch dependent on surface, accounting for
the anisotropy by grid generation techniques will be challenging.
In practice, turbulence in the magnetic field implies a less stringent condition,
but it is difficult to quantify just how much less, and of course even small
perturbations are likely to prove a challenging problem in grid adaptation.


# Slide 9. 
In the next few months, it is of major importance to arrange so that
a diverse community of universities, research institutes such as STFC and UKAEA may 
collaborate effectively on the development of the Neptune software. The next few months
present an opportunity to tune the framework which it is the responsibility of York (as
successful bidder for Calls 83 and 86) to deliver.

Also in the next few months we are looking, particularly through the smaller calls,
to examine options for the software.  Essentially by the end of the summer, I am looking to have
assembled a design justification file of reports. This will explain why we prefer the
options we have selected to other possibilities considered. Most of the bid documents laid out
possible options to explore and gave the bidders the freedom to explore at least one option
of their own choosing. With a view to the longer term, we tried to make it clear that 
UKAEA was willing to consider novel ideas and approaches. Obviously their acceptance is likelier
the more evidence there is that they will perform well at Exascale, and where demonstration
is lacking, we shall endeavour to help provide it.
I want to emphasise that you should take this opportunity. By late summer 2021, we need to be
transitioning to a full-on software development phase, in which we need to be able to say
"We debated and discussed this option already, we took a decision, we stick by it".
Thereafter, if you think some new finding justifies a re-think then you will need to make out a strong case.


# Slide 10.
This slide addresses points raised during the meeting.
Firstly since the meeting announcement did not make clear that slides presented at this meeting
might be made further available on a website intended to become public, presenters 
should feel free to edit their slides with this in view, assuming they wish them published.

Secondly, if you do not have at least a year's experience of the git system for managing
software repositories, please get training. Despite the prestige of its author Torvalds,
the git CLI is not only excessively complex but possessed of many pitfalls even for those
otherwise well-versed in Linux. It should also be noted that the two widespread GUIs, 
Atlassian Bitbucket and gitlab, are subtly incompatible.

There was much mention of the proliferation of acronyms, which we had already noticed in
our internal reports and commenced a collection of these, and mathematical symbols, as
the basis of an ontology for the project. A preliminary collection may be found in the
location tex/index_of_acronyms_and_symbols of git repository https://github.com/ExCALIBUR-NEPTUNE/Documents

As indicated, we hope to keep reporting light in this initial phase, both because of
Lockdown and because of the research-oriented nature of most of the work. There is no exception
to the rule that UKAEA needs to be informed of significant delays, where significant implies
a noticeable impact on contractual deliverables. However, we take the view that negative results
may prove generally informative, so promise to respond to prompt and honest reporting of difficulties
with sympathy and maximal flexibility.

The mid-March meeting has to be scheduled for a day either just before or just after the weekend
of March 13/14. If within the next few days, I don't hear of any clashes with other events,
I'll assume we're free to choose any one of those dates.
