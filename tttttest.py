battlefield = "[a]#b#[c][d]ggg"


def alphabet_war(battlefield):
    def get_shelters(battlefield):
        shelters = []
        start_index = None
        for i, char in enumerate(battlefield):
            if char == '[':
                start_index = i
            elif char ==']':
                if start_index is not None:
                    shelters.append([start_index, i])
                    start_index = None
        return shelters

    def get_gaps(battlefield):
        gaps = []
        start_index = 0
        for i, char in enumerate(battlefield):
            if char == "]":
                if len(battlefield) - 1 == i:
                    start_index = i
                    gaps.append([start_index, i])
                start_index = i
            elif char == "[" or len(battlefield) - 1 == i:
                gaps.append([start_index, i])
        return gaps

    def calculate_bombs_per_gap(battlefield):
        bombs_count_per_gap = []
        gaps = get_gaps(battlefield)
        bombs = get_bombs(battlefield)
        for gap in gaps:
            bombs_count = 0
            for bomb in bombs:
                if bomb in range(gap[0], gap[1] +1):
                    bombs_count += 1
            bombs_count_per_gap.append(bombs_count)
        return bombs_count_per_gap
    def map_bombs_to_shelters(battlefield):
        bombs_per_gap = calculate_bombs_per_gap(battlefield)
        shelters = get_shelters(battlefield)
        safe_shelters = []
        for i, shelter in enumerate(shelters):
            bombs = bombs_per_gap[i] + bombs_per_gap[i+1]
            if bombs < 2:
                safe_shelters.append(shelter)
        return safe_shelters

    def map_safe_shelters(battlefield):
        safe_shelters = map_bombs_to_shelters(battlefield)
        safe_letters = ""
        for shelter in safe_shelters:
            safe_letters = safe_letters + battlefield[shelter[0]+1:shelter[1]]
        return safe_letters

    def get_bombs(battlefield):
        return [bomb_index for bomb_index, char in enumerate(battlefield) if char == "#"]

    if battlefield.count("#") == 0:
        return battlefield.replace("[", "").replace("]", "")
    return map_safe_shelters(battlefield)
