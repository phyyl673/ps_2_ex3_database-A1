import matplotlib.pyplot as plt

def lineplot(df, x, y, hue=None, title=None):
    fig, ax = plt.subplots()
    if hue is None:
        ax.plot(df[x], df[y])
    else:
        for key, group in df.groupby(hue):
            ax.plot(group[x], group[y], label=str(key))
        ax.legend(title=hue)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if title:
        ax.set_title(title)
    return ax

def barplot(df, x, y, title=None):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if title:
        ax.set_title(title)
    return ax
