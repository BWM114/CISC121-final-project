import random
import gradio as gr

MAX_STEPS = 8


def generate_list():
    arr = random.sample(range(1, 101), 5)
    display = f"Random Array:\n{arr}"
    return display, arr


def bubble_sort_on_state(arr_state):
    if not arr_state:
        empty_steps = []
        empty_states = []
        for i in range(MAX_STEPS):
            empty_steps.append("")
            empty_states.append("")
        list_msg = "⚠️ Please click 'Generate Array' first"
        error_msg = "⚠️ No array to sort"
        result = [list_msg]
        result.extend(empty_steps)
        result.extend(empty_states)
        result.append(error_msg)
        return result


    arr = arr_state[:]
    steps = []
    ranges = []
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            steps.append(f"Compare {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                steps.append(f"Swap {arr[j + 1]} and {arr[j]}")
                swapped = True
            ranges.append(f"Current Array: {arr}")
        if not swapped:
            break


    if len(steps) < MAX_STEPS:
        for i in range(MAX_STEPS - len(steps)):
            steps.append("")
    if len(ranges) < MAX_STEPS:
        for i in range(MAX_STEPS - len(ranges)):
            ranges.append("")


    final_steps = []
    for i in range(MAX_STEPS):
        if i < len(steps):
            final_steps.append(steps[i])
        else:
            final_steps.append("")
    final_ranges = []
    for i in range(MAX_STEPS):
        if i < len(ranges):
            final_ranges.append(ranges[i])
        else:
            final_ranges.append("")
    final_msg = f"✅ Sorting Complete: {arr}\nComparisons: {comparisons} | Swaps: {swaps}"
    list_display = f"Original Array:\n{arr_state}"
    result = [list_display]
    result.extend(final_steps)
    result.extend(final_ranges)
    result.append(final_msg)
    return result


with gr.Blocks(title="Bubble Sort Visualization") as demo:
    gr.Markdown(
        """
        # 🎯 Bubble Sort Visualization
        **Step 1:** Click **Generate Array** (5 unique numbers 1-100)  
        **Step 2:** Click **Run Bubble Sort**  
        View each comparison and swap step, and array state after each pass
        """
    )

    arr_state = gr.State([])


    with gr.Row():
        gen_btn = gr.Button("Generate Array 🎲", variant="secondary")
        run_btn = gr.Button("Run Bubble Sort 🔄", variant="primary")


    list_box = gr.Textbox(label="Generated Array", lines=2, interactive=False)
    gr.Markdown("### 🔹 Sorting Steps")
    step_boxes = []
    for i in range(MAX_STEPS):
        step_boxes.append(gr.Textbox(label=f"Step {i + 1}", lines=1, interactive=False))
    gr.Markdown("### 🔸 Array States")
    range_boxes = []
    for i in range(MAX_STEPS):
        range_boxes.append(gr.Textbox(label=f"State {i + 1}", lines=1, interactive=False))
    result_box = gr.Textbox(label="Final Result", lines=2, interactive=False)


    gen_btn.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_box, arr_state],
    )
    run_btn.click(
        fn=bubble_sort_on_state,
        inputs=[arr_state],
        outputs=[list_box] + step_boxes + range_boxes + [result_box],
    )

if __name__ == "__main__":
    demo.launch(share=True)