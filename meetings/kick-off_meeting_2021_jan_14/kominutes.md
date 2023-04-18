# Agenda, 14 January 2021

 - Wayne Arter, UKAEA 	9.05-9.20	Introduction
 - Ben Dudson,  York 	9.20-9.45	Plasma fluid referent model via exploratory proxyapps
 - Steven Wright, York 	9.45-10.00	Investigate DSL and code generation techniques
 - 	---Break---
 - Dave Moxey, Exeter 	10.20-10.50 	Performance of Spectral Elements
 - Felix Parra, Oxford	10.50-11.10	Referent model for plasma edge region
 - 	---Break---
 - Peter Challenor, Exeter 11.20-11.35	UQ (UKAEA funding outside  ExCALIBUR)
 - Sue Thorne,  STFC 	11.35-11.50	Investigate matrix-preconditioning techniques
 - Peter Coveney, UCL	11.50-12.05	Study of Uncertainty Quantification (UQ) techniques
 - Serge Guillas, UCL 	12.05-12.20	Study of Model Order Reduction (MOR) Techniques
 - Ben McMillan, Warwick 	12.20-12.35	Optimal Use of Particles
 - 	---Short break---
 - Discussion 		12.40-end

*Slides of the talks, where subsequently submitted, appear as files
listed by first speaker's surname.

# Rob Akers PI Neptune in chair
indicated that the importance of this meeting to the project as
two-thirds of Neptune was to be sourced outside UKAEA. In particular,
the presenters should explain their proposed contributions to Neptune,
concentrating particularly on first 6-9 months.

# Wayne Arter
was introduced as technical lead for Neptune.
[The script for Wayne Arter's introductory talk appears in this (KOM)
directory as intro_wa.md (Markdown format).]
He thanked the attendees for their bid work and remarked upon its high quality
despite the circumstances. He emphasised that the attendees should take the
opportunity in the next few months to examine options for the software, as
by late summer 2021, Neptune needed to be
transitioning to a full-on software development phase.

# Ben Dudson
focussed on the most complicated model in his portfolio, which includes
nonlinear, time dependent, highly anisotropic tensor coefficients, and
the challenges presented to finite elements, notably SHP (spectral/hp
element). He particularly indicated the relationship with the work
packages of other presenters, nicely summarised on one slide:

 - Conventional neglect of the (speed of) light-timescale leads to an elliptic problem
for the electric potential which may be a major bottleneck, hence good
preconditioning important.
 - Sources from the particle model involve reaction rates with uncertainties.
 - The multispecies aspect leads to additional complexity where DSL could be helpful.
 - The kinetic proxyapp would benefit from development of a gyro-averaged model.

## Peter Hill (dudson.pdf)
explained the Excalibur-Neptune github 'organisation' which he was
setting up, as an "umbrella" for entire project, so that the downloader of
Excalibur-Neptune/Neptune gets all the software used by the project.
Individual repositories (repos) become submodules of the github organisation,
e.g. Documentation, with Nektar++ expected.
The project encourages use of a common open-source licence BSD 3 - "do
what you like, but must acknowledge, and not use name if change source"
All issues should be raised in Excalibur-Neptune/Neptune, and
classified as "being done", "done" etc.
The standard github development workflow was explained, with a
recommendation for test-driven development, with
automated testing by github actions.
A common code style will be enforced using clang-format or black, and
the recommendation is to use latest language standards such as C++20 and
Fortran 2018 as far as Exascale machines permit.

## Discussion
Slack was mentioned for user feedback.
Peter Coveney provoked a discussion on accessible HPC hardware.
Rob Akers explained that all bid respondents offered to use their own
machines, and noted that UKAEA was contributing £1M per year to CSD3
(Cambridge Service for Data-Driven Discovery) for use under DiRAC
so that 6000 cores of Cascade Lake were available and 2 racks of the latest 60Gbtye
Nvidia Ampere cards were to arrive in Spring. Neptune may however also have to use
ARCHER2 because of "turbulence" in EPSRC budget.
Peter Coveney stated that Europe will have 3 machines comparable to US
Summit this year, but UK use of these machines is subject to negotiation.

# Steven Wright
introduced himself as from York Computer Science dept.
His task was to coordinate code development and set standards,
beginning with a survey of available hardware and software, including DSLs and proxyapps
particularly ones directed towards software with characteristics of BOUT++ and Nektar++.
The metric to be used was due to Pennycook, Sewall & Lee et al Future Gen Computer Systems 2019
https://doi.org/10.1016/j.future.2017.08.007
He expected coordination, especially when related to
providing a programming model, to involve extensive user feedback, to be provided via Slack.

# Introductions at Break

 - Chris Cantwell introduced himself as having 10 years' experience of
spectral elements, intending to be working on proxyapps for Neptune.
 - Gihan Mudalige introduced himself as working on several Excalibur projects,
for Neptune specifically DSLs.
 - Nigel Woods introduced himself as
looking after the science side of the Met Office's weather and climate
Excalibur use case, and publicised recent appearence of the Excalibur cross-cut call.
 - Louise Kimpton introduced herself
as a recent Peter Challenor PhD, who had just become a postdoc working with Tim Dodwell.

# David Moxey
with Chris Cantwell and Spencer Sherwin, will focus on a
prototypical 2-D anisotropic heat transport problem.  He gave a brief
introduction to spectral/hp element methods (SHP) with reference to techniques for
generating meshes with curved edges and surfaces, notably by
variational weighted optimisation within Nekmesh (weight corresponding
to linear- or hyper-elasticity or Winslow or Laplacian smoothing). He
illustrated mesh r-adaptation including nodes that slid along a surface,
with particular reference to treating the vicinity of the X-point for
Neptune. Concerning the spectral element calculation, he planned to
extend efficient matrix-free implementation from x86 to GPU and other
architectures. Regarding engagement with other partners, he mentioned
use of CWIPI for code coupling. He also introduced Nektar++ as a
open-source framework for high-order finite element methods for wide application, and
mentioned recent developments facilitating use by docker, and Jupyter
(nearly complete, but remaining a work in progress) with continuous
delivery as well-advanced, for automating the entire software release
process. He advertised a vacancy for a post-doc to work with him on Neptune.

In response to Rob Akers' question regarding adaptive meshing, David Moxey
indicated that he was developing adaptive r-refinement, but that he currently
mainly used p-adaptation, with a longer term plan for coupled h-adaptation driven by
errors detected in the numerical solution.
Replying to Wayne Arter, he agreed that training needs should be expressed via Slack
channels, and although difficult for Dave Moxey to address in short terms
beyond say a two-hour seminar, things should ease after say Easter, when
other Nektar++ project members should be able to help.
In response to Rob Akers' question regarding separation of concerns,
Dave Moxey stated that combining e.g. Kokkos with pre-existing code such as Nektar++ could be
difficult. Two possibilities to be investigated were the identification of kernels
that could be optimised for GPU, and better memory management based on  discussions
planned with Nvidia.
Rob Akers encouraged discussion of separation of concerns.

# Felix Parra
apologised for absence of Michael Barnes and postdoc Michael Hardman due to
teaching commitments, and introduced himself as a physicist principally
concerned with analytic calculation.
He explained that kinetic effects matter when lack of collisions means that
contributions from particles distant from a point are important at the
point, and plasma has additional complication of electromagnetic (EM) effects.
Collisionality is low in the core plasma, and the fluid
approximation may also break down in the divertor where electrons (and ions) are
energetic and so collide less. He does not think a simple fluid model with
corrections will be adequate.  Plasma presents the problem of quasi-neutrality
when the light timescale is neglected, which implies that there must be a very
accurate balance between positive and negative charge in the plasma.
Plasma confinement by large magnetic field B implies a short lengthscale of
gyro-radius of ion motion which can be avoided by gyro-averaging, likely best done
analytically.
He presented a schematic form of kinetic equations noting the appearance of
the perpendicular drift velocity resulting from gyro-averaging.
The tininess of any net charge implies not only a
near-solenoidal electric field E, but also a near divergence-free current,
and there results a very stiff equation for the time evolution of the electric
potential. The aim of his analytic approach is try to avoid this stiffness by
splitting particle distribution function into kinetic and fluid parts in
a special way indicated.

Wayne Arter's question revealed that Felix Parra's fluid is not necessarily Maxwellian.
The deviation of the particle distribution function from Maxwellian is very involved
in the core but probably more simply skewed in the edge region. Though the
electric field may be large in the edge, it is believed that quasi-neutrality
fails only on short electron timescales.
As a result of question by Rob Akers, Ben Dudson mentioned the existence of Swiss work
on gyro-averaged models for the plasma edge.

Rob Akers emphasised importance of UQ to UKAEA programme going
forwards, consequently that Peter Challenor was present as a result
of funding directly from UKAEA budget.

# Peter Challenor
defined the direct problem y=f(x), and the inverse problem as, given
measurements of y to find corresponding x.
Uncertainty Quantification (UQ) was defined as the subject of treating
prediction with uncertainty, sensitivity analysis, uncertainty
analysis, and inverse modelling with uncertainty.
Fast models use Monte-Carlo (MC), Markov Chain MC (MCMC), and Quasi-MC (QMC).
To proceed with slow problems need to
produce fast surrogates that include a measure of uncertainty, referred to as
'emulators'. Neural networks (NNs) tend not to include uncertainty
measures, hence Gaussian Process Emulation (GPE) preferred.

- f(.) as a  sum of a mean function + zero mean Gaussian Process (GP)
with covariance function C(.,.) + 'nugget' is white noise term.

C(.,.) may be Gaussian in cases of smooth f. For more irregular f behaviour,
the square in the Gaussian should not simply be replaced by modulus but rather
the Gaussian replaced by a special function after Matern.
Priors for GPE are form of mean function (which could be a Fourier series or
polynomial), C(.,.), and the nugget amplitude.
Analysis typically proceeds by designing a training
set, building the emulator, and validating use LOO = "leave one out" or by
conducting other experiments. Designs use Latin hypercube sampling, Sobol,
sequential sampling.
Emulation may not work because of model discrepancy. The widely used
approach of Kennedy and O'Hagan has problems that means Peter Challenor
prefers to use "History Matching", also this has problems
of statistical interpretation and also caused by empty sets of NROY= "not ruled out yet".
History matching can cope with  hierarchical models and with a mix of fidelities.
Rob Akers indicated work could be useful to STEP, was reassured that
the use of Gaussians ensured extrapolation beyond boundaries of the data
prevented dramatically divergent behaviour, however it did pose
difficulties for imposing positivity constraints.

# Sue Thorne
gave apologies for Anton Lebedev and Emre Sahin.
Preconditioning speeds iterative solution of Ax=b for x, find B= inv(P) A so
By=c goes faster for y= inv(Q) x. Coupling is an important issue, gives rise to a block
structure in A to try to exploit.
Preconditioning within a block may use knowledge of physics of system
(elliptic/hyperbolic, elliptic particularly allows use of multigrid) or
involve SPAI (sparse approximate inverse) or use
MCMCMI (MCMC for approximate matrix inversion) to approximate inv(A).
Neumann series for diagonally dominant matrices, implemented using
MPI, OpenMP and range of GPUs,
see Vassil and Vassil https://ieeexplore.ieee.org/document/8638012,
outperforms MSPAI (Monte-Carlo SPAI).
Implicit-factorisation to treat both loosely and strongly coupled, also
hope to examine novel reduced subspace iteration. Example of a 3x3 block
system where 3rd row and column specially constrained.
Rob Akers' question revealed MCMCMI as a new (2018) and exciting
approach.
Patrick Farrell asked how MCMCMI worked matrix-free, but the STFC team
were momentarily unable to provide a detailed answer, and it was
suggested by Rob Akers that the question be pursued via Slack.

# Peter Coveney
introduced Maxime Vassaux, who revealed he had MD experience coupling
particle and continuum models for materials.
Objective to recommend UQ techniques for Neptune longer-term, and for
workflows, not only EasyVVUQ which is being developed under Framework
programme project VECMA but also Multi-output GP (MOGP) from ATI.
V & V as verification (that equations are correctly solved)  and
validation (by comparison with experiment).
[Barry Boehm defines validation as answering the question "Are we
building the right product?", and verification as "Are we building the
product right?"]

Two classes of uncertainty recognised, namely

 - Systemic - uncertainty in parameters
 - Aleatoric - random, stochastic contribution

He publicised UQ Neptune workshop on 18/1/21 and VECMA Hackathon
19/1/21 where attendees should find EasyVVUQ to be "easy" to use.
VECMA is an open development (notably involving Coster and Lakhlili
from the German fusion lab IPP), producing a modular toolkit called
VECMAtk which allows complex workflows and includes "Pilot job" for
managing a campaign, typically an ensemble of UQ calculations.
He described two pieces of work applying VECMA to (1) high systemic
uncertainty - Neill Ferguson's CovidSim about 15 minutes on single
node, noting the importance of parameter identification, finding 940
which were reduced down to 20 significant ones by expert discussion and
a dimension adaptive methodology, see Edeling et al
https://www.researchsquare.com/article/rs-82122/latest.pdf
and (2) high aleatoric uncertainty - MD simulation using 2 million
core-hours, identifying most important parameters.

# Serge Guillas
Introduced Deyu Ming, joining the project on 1st February, who revealed
he has been working on statistics of coupling tsunami to earthquake.
Serge Guillas noted Deyu's linkage via earthquake modelling work with Eric
Daub, and his own Met Office link.
He emphasised the n-cubed scaling of GP fitting if f n-dimensional, and
two publications related to MOR, for

 - Dimension reduction, see Liu & Guillas - http://www.siam.org/journals/juq/5/M109064.html, and
 - Sequential design, see Beck & Guillas http://www.siam.org/journals/juq/4/98961.html,
where parameters are chosen on the basis of previous simulations.

1. Dimension reduction of outputs (wave heights) in Cascadia tsunami
temporal problem, using
Outer product emulator (OPE) f = Sum (alpha g) + e , alpha=Sum (beta g)
where choice of basis g may be splines, polynomials etc depending on
problem.
Use of functional principal components beats Fourier, as
validated by LOO. OPE also successfully applied to a spatial problem,
namely parameterised gravity waves from NCAR climate model CSM which is
1.2M lines of code, calibrating using spherical harmonics.
2. Dimension reduction of inputs (sample sea depths) in tsunami
prediction using synthetic bathymetry, where 150
training runs reduced 3200 inputs to 5, then emulator was built using
gKDR (gradient-based kernel dimension reduction). This approach was
compared with others on a range of test problems and generally found to
be superior.
3. In MOR for multi-physics or even multi-disciplinary applications, it
was found to be very powerful to use  knowledge of components of system
to construct a "linked emulator" (term now preferred to "integrated
emulator" as used in the slides), see Ming & Guillas
https://arxiv.org/pdf/1912.09468

# Ben McMillan
with Tom Goffrey, advised by Tony Arber with computational expert Keith
Bennett.
Ben McMillan described use of particles to deal with kinetic effects, noting the
usefulness of reducing 6-D phase-space to 5-D by gyro-averaging, here
solving the resulting problems by a Lagrangian (particle) method, cf.
Felix Parra is using Eulerian approach.
Ben McMillan described a PIC (Particle-in-Cell) code, where
(macro-)particles are driven by an electromagnetic (EM) force, using
an EM field calculated typically on a finite difference grid.
He referred to Arber's 2015 review article
https://iopscience.iop.org/article/10.1088/0741-3335/57/11/113001
which acts as a reference for Warwick's EPOCH (6-D) PIC code, important
as Neptune work will employ an EPOCH proxyapp.
[The review by Wayne Arter http://dx.doi.org/10.1088/0034-4885/58/1/001
although older covers particle modelling for fusion in Sec.3.]
Ben McMillan  explained how gyro-averaged (5-D) PIC moves "rings of charge", and
how he has extensive experience of the implementation in ORB5 software,
which will be transferred to EPOCH proxyapp.
Ben saw his project work as intended to demonstrate proof-of-principle
for algorithmic features of particle substepping, Jacobian-free
Newton-Krylov (JFNK) for implict PIC solution, gyro-averaging, delta-f
(control variates as perturbations to fluid model), and ultimately to
help design coupling to SHP.

# Concluding Remarks
[The slide Wayne Arter presented at this point is joined to the end of his
introductory talk slides.] 
Wayne Arter in points arising, noted that presenters were allowed to edit slides
before they became part of the Neptune "archive" however ultimately defined.
He recommended training in git for all but the most experienced users.
He drew attention to the "sub module" repo Excalibur-NEPTUNE/Documents,
particularly a collection of acronyms and symbols in subdirectory tex
He emphasised that at least for the current FY, project reporting
would be lightened as far as possible, to help with consequences of lockdown.


Rob Akers thanked presenters and encouraged submission of slides within the week,
reminded attendees that Neptune was a £5M project continuing until at
least 2024. Invoices should be in by 19th March, slides presented at the March workshop
acceptable as deliverables provisionally.   Peter Hill mentioned that
readthedocs will have to be public, so in Neptune subdirectory of
Excalibur-Neptune, suggested acronyms and symbols moved to readthedocs.
