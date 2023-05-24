# Graphs
import matplotlib.pyplot as plt
import numpy as np

# Colour for each type
# Original
# incremental
# pipelined
# pipelined and OOO


## Read and write throughput
## table of miss rates
# experiment     | root miss interval  |  leaf miss interval
# --------------------------------------------
# every leaf     |   512*128           |  512
# every root     |  512                |  4
# every leaf line|  128                |  1
# every root line|  1                  |  1


width = 0.1
multiplier = 0


def plot_bunch(
    group_num,
    tpts,
    ax,
    designs=["Original", "Improved single-cache", "Simple pipelined", "OOO Pipelined"],
    hatchs=["/", "|", "x", "."],
    colours=["tab:blue", "tab:green", "tab:orange", "tab:red"],
    width=0.1,
    outline_width=0,
):

    offset = width * (len(designs) + 1) * group_num
    xs = offset + np.arange(len(designs)) * width
    for x, (tpt, (lab, (col, h))) in zip(
        xs, zip(tpts, zip(designs, zip(colours, hatchs)))
    ):
        rect = ax.bar(
            x,
            1 / tpt,
            width,
            label=lab,
            color=col,
            hatch=h,
            lw=outline_width,
            edgecolor="black",
            alpha=0.6,
        )
        ax.bar_label(rect, fmt="%.1f")


def plot_bar_chart(
    title,
    save_name,
    experiments,
    throughputs,
    xlabel,
    designs=[
        "Original",
        "Improved single-cache",
        "Simple pipelined",
        "Out-of-order pipelined",
    ],
    hatchs=["//", "**", "xx", ".."],
    colours=["tab:blue", "tab:green", "tab:orange", "tab:red"],
    # colours=["gainsboro", "gainsboro", "gainsboro", "gainsboro"],
    figsize=(10, 6),
    width=0.1,
    outline_width=1,
    y_max=40,
    y_interval=5,
):
    fig, ax = plt.subplots(layout="constrained", figsize=figsize)
    multiplier = 0
    for i, tpts in enumerate(throughputs):
        multiplier = plot_bunch(
            i,
            tpts,
            ax,
            designs=designs,
            hatchs=hatchs,
            colours=colours,
            outline_width=outline_width,
        )
        if i == 0:
            ax.legend()
        # ax.legend(
        #     loc="upper center",
        #     # bbox_to_anchor=(0.5, -0.05),
        #     bbox_to_anchor=(0.5, -0.1),
        #     fancybox=True,
        #     ncol=4,
        # )
    # plt.axhline(y=1.0, ls="--")
    ax.set_ylabel("Average cycles per responses")
    ax.set_xlabel(xlabel)
    ax.set_title(title)

    xtick_offset = 1.5 * width
    xtick_stride = 5 * width
    xticks = np.arange(len(experiments)) * xtick_stride + xtick_offset

    ax.set_xticks(xticks, experiments)
    ax.set_yticks(np.arange(0, y_max + y_interval, y_interval))
    plt.savefig(f"Logs/figures/bar_{save_name}.png")


## ROOT ONLY READS
title = "All leaf tags are zero"
save_name = "root_reads"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [0.3329, 0.9995, 0.9995, 0.9993],
    # every root
    [0.3247, 0.9208, 0.9174, 0.9111],
    # every leaf line
    [0.3015, 0.7574, 0.7483, 0.7329],
    # every root line
    [0.0233, 0.0233, 0.0208, 0.0626],
]
xlabel = "Stride length"
experiments.reverse()
throughputs.reverse()
y_max = 50
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)

## ROOT ONLY WRITES
title = "Root only write requests"
save_name = "root_writes"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [0.3329, 0.9956, 0.9996, 0.9995],
    # every root
    [0.3247, 0.9208, 0.9174, 0.9111],
    # every leaf line
    [0.3012, 0.7395, 0.7603, 0.7433],
    # every root line
    [0.0233, 0.0248, 0.0223, 0.0670],
]
experiments.reverse()
throughputs.reverse()
xlabel = "Stride length"
y_max = 50
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)


## BOTH reads
title = "All root tags are one"
save_name = "both_reads"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [0.1971, 0.4807, 0.9176, 0.9111],
    # every root
    [0.0698, 0.0795, 0.0780, 0.0727],
    # every leaf line
    [0.0236, 0.0226, 0.0207, 0.0742],
    # every root line
    [0.0116, 0.0116, 0.0118, 0.0346],
]
experiments.reverse()
throughputs.reverse()
xlabel = "Stride length"
y_max = 90
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)

## BOTH writes
title = "Root and leaf write requests"
save_name = "both_writes"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [0.1971, 0.4807, 0.9176, 0.9111],
    # every root
    [0.0698, 0.0795, 0.0780, 0.0727],
    # every leaf line
    [0.0236, 0.0226, 0.0207, 0.0742],
    # every root line
    [0.0116, 0.0116, 0.0118, 0.0346],
]
experiments.reverse()
throughputs.reverse()
xlabel = "Stride length"
y_max = 90
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)
