import numpy.core.numeric as _nx
def array_split(ary, indices_or_sections, axis=0):
    """
    Split an array into multiple sub-arrays.
    Please refer to the ``split`` documentation.  The only difference
    between these functions is that ``array_split`` allows
    `indices_or_sections` to be an integer that does *not* equally
    divide the axis.
    See Also
    --------
    split : Split array into multiple sub-arrays of equal size.
    Examples
    --------
 x = np.arange(8.0)
 np.array_split(x, 3)
        [array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.])]
    """
    try:
        Ntotal = ary.shape[axis]
    except AttributeError:
        Ntotal = len(ary)
    try:
        # handle scalar case.
        Nsections = len(indices_or_sections) + 1
        print "Hurray" 
        div_points = [0] + list(indices_or_sections) + [Ntotal]
    except TypeError:
        # indices_or_sections is a scalar, not an array.
        Nsections = int(indices_or_sections)
        if Nsections <= 0:
            raise ValueError('number sections must be larger than 0.')
        Neach_section, extras = divmod(Ntotal, Nsections)
        section_sizes = ([0] +
                         extras * [Neach_section+1] +
                         (Nsections-extras) * [Neach_section])
        div_points = _nx.array(section_sizes).cumsum()

    sub_arys = []
    sary = _nx.swapaxes(ary, axis, 0)
    for i in range(Nsections):
        st = div_points[i]
        end = div_points[i + 1]
        sub_arys.append(_nx.swapaxes(sary[st:end], axis, 0))

    # This "kludge" was introduced here to replace arrays shaped (0, 10)
    # or similar with an array shaped (0,).
    # There seems no need for this, so give a FutureWarning to remove later.
    if sub_arys[-1].size == 0 and sub_arys[-1].ndim != 1:
        warnings.warn("in the future np.array_split will retain the shape of "
                      "arrays with a zero size, instead of replacing them by "
                      "`array([])`, which always has a shape of (0,).",
                      FutureWarning)
        sub_arys = _replace_zero_by_x_arrays(sub_arys)

    return sub_arys

print array_split(range(100), [33,66,99])
