fn are_all_characters_unique(string: &str) -> bool {
    for (index, character) in string.chars().enumerate() {
        let slice = &string[index + 1..];
        if slice.find(character) != None {
            return false;
        }
    }
    return true;
}

fn find_start_of_package(string: &str) {
    let slice = &string[3..string.len()];
    for (index, _letter) in slice.chars().enumerate() {
        let window = &string[index..index + 4];
        if are_all_characters_unique(window) {
            println!("Unique sequence found at index {}", index + 4);
            return;
        }
    }
    println!("No unique sequence found");
}

fn main() {
    let file_contents = std::fs::read_to_string("input_day6.txt").expect("File not found");
    find_start_of_package(&file_contents);
}
