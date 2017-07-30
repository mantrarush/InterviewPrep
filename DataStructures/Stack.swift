protocol StackProtocol {
    func push(item: Int)
    func pop() -> Int?
    var peek: Int? { get }
    var count: Int { get }
}

class Stack: StackProtocol, Equatable {
    private var data: [Int] = [Int]()
    
    var count: Int {
        return data.count
    }
    
    func push(item: Int) {
        data.append(item)
    }
    
    func pop() -> Int? {
        guard let lastItem: Int = peek else { return nil }
        data.remove(at: count - 1)
        return lastItem
    }
    
    var peek: Int? {
        return data.last
    }
    
    static func ==(lhs: Stack, rhs: Stack) -> Bool {
        return lhs.data == rhs.data
    }
}

func stackUsageExamples() {
    let someStack: StackProtocol = Stack()
    print(someStack.peek)
    print(someStack.push(item: 32))
    print(someStack.count)
    print(someStack.peek)
    print(someStack.pop())
}
