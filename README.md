# needextract_347

Ref - https://github.com/useblocks/sphinxcontrib-needs/issues/348

Test case to illustrate error message with sphinx=4.0.2 and sphinxcontrib-needs, commit 8568810dcb6a39fd6643f341c429d22a9809d0ff

The approach in commit 8568810dcb6a39fd6643f341c429d22a9809d0ff does not properly render this table.  See SRD.tex and its PDF rendering here:  https://www.overleaf.com/read/bbjxhkdgyvbt

An alternate latex approach (emulating the standard Sphinx rendering) that works as desired (i.e., table is rendered and shows up in List of Tables) is shown in SRD_mod.tex, available at the link above.  This approach uses the following, starting at line 175 of SRD_mod.tex:

.. code-block::

    \begin{figure}[H]
    \centering
    \sphinxcapstartof{table}
    \sphinxthecaptionisattop
    \sphinxcaption{My Table from sphinxneeds\sphinxhyphen{}contrib \textquotesingle{}needtable\textquotesingle{} directive}\label{\detokenize{srd_main:needtable-srd_main-0}}
    \sphinxaftertopcaption

    \begin{savenotes}\sphinxattablestart
    \centering
    \begin{tabulary}{\linewidth}[t]{|T|T|T|T|T|T|}

    ...

    \end{tabulary}
    \par
    \sphinxattableend\end{savenotes}
    \end{figure}
