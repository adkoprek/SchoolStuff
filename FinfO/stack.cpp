#include <vector>


class Stack {
public:
    Stack() {
        m_list = new std::vector<double>();
    }

    ~Stack() {
        delete m_list;
    }

    void push(double element) {
        m_list->push_back(element);
    }

    double pop() {
        double last_element = m_list->back();
        m_list->pop_back();
        return last_element;
    }


private:
    std::vector<double>* m_list;
};

int main() {
    Stack stack;
}
