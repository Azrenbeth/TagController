# Copyright 2023 William Ashton

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


# width = 0.1
# multiplier = 0


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
            tpt,
            width,
            label=lab,
            color=col,
            hatch=h,
            lw=outline_width,
            edgecolor="black",
            alpha=0.6,
        )
        ax.bar_label(rect, fmt="%.2f")


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
    figsize=(10, 4),
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
            width=width,
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
    ax.set_ylabel("Mean cycles between responses")
    ax.set_xlabel(xlabel)
    ax.set_title(title)

    xtick_offset = 1.5 * width
    xtick_stride = 5 * width
    xticks = np.arange(len(experiments)) * xtick_stride + xtick_offset

    ax.set_xticks(xticks, experiments)
    ax.set_yticks(np.arange(0, y_max + y_interval, y_interval))
    plt.savefig(f"Logs/figures/bar_{save_name}.png")


## ROOT ONLY READS
title = "All root tags are zero"
save_name = "root_reads"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [
        3.0036003600360037,
        1.0005000500050005,
        1.0005000500050005,
        1.0007000700070008,
    ],
    # every root
    [
        3.07960796079608,
        1.086008600860086,
        1.09000900090009,
        1.0976097609760977,
    ],
    # every leaf line
    [
        3.3163163163163163,
        1.3203203203203202,
        1.3363363363363363,
        1.3643643643643644,
    ],
    # every root line
    [
        43.0,
        43.0,
        48.002002002002,
        15.96896896896897,
    ],
]
xlabel = "Stride length"
# experiments.reverse()
# throughputs.reverse()
y_max = 50
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)

## BOTH reads
title = "All root tags are one"
save_name = "both_reads"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [
        5.073407340734073,
        2.08030803080308,
        1.0898089808980898,
        1.0976097609760977,
    ],
    # every root
    [
        14.328232823282328,
        12.57905790579058,
        12.822982298229823,
        13.746774677467748,
    ],
    # every leaf line
    [
        42.308308308308305,
        44.294294294294296,
        48.252252252252255,
        13.485485485485485,
    ],
    # every root line
    [
        86.0,
        86.0,
        85.0,
        28.92792792792793,
    ],
]
# experiments.reverse()
# throughputs.reverse()
xlabel = "Stride length"
y_max = 90
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)


## ROOT ONLY WRITES
title = "All root tags are zero"
save_name = "root_writes"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [
        3.0,
        1.0,
        1.0,
        1.0,
    ],
    # every root
    [
        3.077558934585162,
        1.087253801408307,
        1.0913358505969997,
        1.0988876415960813,
    ],
    # every leaf line
    [
        3.300375469336671,
        1.3304130162703378,
        1.3529411764705883,
        1.3829787234042554,
    ],
    # every root line
    [
        43.0,
        43.0,
        48.0,
        15.993742177722154,
    ],
]
# experiments.reverse()
# throughputs.reverse()
xlabel = "Stride length"
y_max = 50
plot_bar_chart(title, save_name, experiments, throughputs, xlabel, y_max=y_max)


## BOTH writes
title = "All root tags are one"
save_name = "both_writes"
experiments = ["16 B", "2 KiB", "8 KiB", "1 MiB"]
throughputs = [
    # every leaf
    [
        4.088208820882088,
        2.0838083808380836,
        1.0922092209220922,
        1.1048104810481048,
    ],
    # every root
    [
        15.38033803380338,
        12.757975797579759,
        13.68056805680568,
        14.150215021502149,
    ],
    # every leaf line
    [
        48.748435544430535,
        44.3153942428035,
        52.25531914893617,
        17.813516896120152,
    ],
    # every root line
    [
        94.43804755944932,
        88.11264080100125,
        106.63579474342929,
        44.53316645807259,
    ],
]
# experiments.reverse()
# throughputs.reverse()
xlabel = "Stride length"
y_max = 110
y_interval = 10
plot_bar_chart(
    title,
    save_name,
    experiments,
    throughputs,
    xlabel,
    y_max=y_max,
    y_interval=y_interval,
)

## BOTH writes
title = "Overtaking the leaf cache"
save_name = "overtake_leaf"
experiments = ["1", "5"]
throughputs = [
    # every leaf
    [
        4.088208820882088,
        2.0838083808380836,
        1.0922092209220922,
        1.1048104810481048,
    ],
    # every root
    [
        15.38033803380338,
        12.757975797579759,
        13.68056805680568,
        14.150215021502149,
    ],
    # every leaf line
    [
        48.748435544430535,
        44.3153942428035,
        52.25531914893617,
        17.813516896120152,
    ],
    # every root line
    [
        94.43804755944932,
        88.11264080100125,
        106.63579474342929,
        44.53316645807259,
    ],
]
# experiments.reverse()
# throughputs.reverse()
xlabel = "Stride length"
y_max = 110
y_interval = 10
plot_bar_chart(
    title,
    save_name,
    experiments,
    throughputs,
    xlabel,
    y_max=y_max,
    y_interval=y_interval,
)
