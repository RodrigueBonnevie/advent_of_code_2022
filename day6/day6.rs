fn are_all_characters_unique(string: &str) -> bool {
    for (index, character) in string.chars().enumerate() {
        let slice = &string[index + 1..];
        if slice.find(character) != None {
            return false;
        }
    }
    return true;
}

fn find_start_of_marker(string: &str, marker_len: usize) {
    let slice = &string[marker_len - 1..string.len()];
    for (index, _letter) in slice.chars().enumerate() {
        let window = &string[index..index + marker_len];
        if are_all_characters_unique(window) {
            println!("Unique sequence found at index {}", index + marker_len);
            return;
        }
    }
    println!("No unique sequence found");
}

fn main() {
    let file_contents = std::fs::read_to_string("input_day6.txt").expect("File not found");
    println!("Searching for start of package...");
    find_start_of_marker(&file_contents, 4);
    println!("Searching for start of message...");
    find_start_of_marker(&file_contents, 14);
}
