# Earthquake recurrence intervals using the Alias method

Python code for calculating recurrence interval (RI) and coefficiant of variation (CV) from C14 dates discrete distributions.

The code is based on the <a href=https://en.wikipedia.org/wiki/Alias_method>Alias</a> random sampling scheme, and on the following publication:
> Biasi, G.P., 2013. Appendix H: maximum likelihood recurrence intervals for California paleoseismic sites. In: US Geol. Surv. Open-file Rept. 2013-1165-H and Calif. Geol. Surv. Special Rept. 228-H.

It includes a jupyter notebook with an example of calculating RI and CV that can be changed according to need.
There are some example .prior files in the `files` directory that were generated with <a href=https://c14.arch.ox.ac.uk/oxcal/OxCal.html>OxCal</a>.

The end of the notebook contains a short discussion about how to represent measurements of offset features for random sampling and includes some examples of common distributions. This is intended for people who are interested in using the random sampling to model slip-rate based on earthquake record.

MIT License
Copyright (c) 2019 Neta Wechsler
