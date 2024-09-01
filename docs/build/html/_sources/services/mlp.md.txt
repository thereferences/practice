# Machine Learning Dependent Projects

## Focus

In brief:

> Focusing on projects that **(a)** address a business problem, **(b)** have an unambiguous problem statement, **\(c\)** have a 
> deployment goal, **(d)** a machine learning model prediction/forecast/diagnostic aim, **(e)** are technologically feasible and economically viable.

<br>

```{mermaid}
%%{ init: { 'flowchart': { 'curve': 'monotoneX'} } }%%
flowchart LR    
    id0([start]) --> id1{<span title="Does the potential project have a budget?">budget</span>} 
    id1 -- yes --> id2{<span title="Is the budget, project timebox, and the collaboration commitment plausible?">budget,<br>time</span>}
    id1 -- no --> id3([terminate])
    id2 -- no --> id3
    id2 -- yes --> id5(<span title="The project scope/design details">project<br>details</span>)
    id5 --> id6{<span title="Is the potential project addressable via machine learning, technically feasible, and economically viable?">feasible?</span>}
    id6 -- no --> id3
    id6 -- yes --> id8(next <br> steps)
    
    classDef default fill:#333333,stroke:#333333,stroke-width:0px,color:#ffffff,font-size:11pt;
```

<br>
<br>

## Service

In collaboration with the client team, please preliminarily assess service requests, for  _machine learning dependent 
projects_, via:

<ul class="disc">
    <li class="disc">The upcoming <i>project details hub</i> of the Scottish Artificial Intelligence Register; for eliciting project 
details.</li>
    <li class="disc">A technological feasibility & economic viability assessment, using the project details.</li>
</ul>

The <a href="https://thereferences.github.io/systems" target="_blank">complementary online pages of the <i>project details 
hub</i></a> is an important, and continuously developing, resource that aids critical assessments of potential machine learning dependent projects.  Once it is ready, a future blog will introduce the <i>project details hub</i>; and discuss the import of feasibility/viability assessments.

Note, a key aspect of a project's _details_ is the identification of the groups/people/partners that will be responsible for 
different parts of the project, and their costs thereof.  The data science team must carefully consider its existing commitments before making a prospective commitment.

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
