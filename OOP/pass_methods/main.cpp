#include <iostream>
using namespace std;

void chargeByValue(int energy) {
    energy += 20;
    cout << "[chargeByValue] 🔋 Заряд увеличен до: " << energy << " (локально)" << endl;
}

void chargeByReference(int& energy) {
    energy += 20;
    cout << "[chargeByReference] ⚡ Заряд увеличен до: " << energy << " (реально)" << endl;
}

void chargeByAddress(int* energy) {
    *energy += 20;
    cout << "[chargeByAddress] 🔧 Заряд увеличен до: " << *energy << " (по указателю)" << endl;
}

int main() {
    int roboEnergyA = 50;
    int roboEnergyB = 50;
    int roboEnergyC = 50;

    cout << "🤖 Робот А. Начальный заряд: " << roboEnergyA << endl;
    chargeByValue(roboEnergyA);
    cout << "После pass by value: " << roboEnergyA << " ⚠️ (не изменился)" << endl << endl;

    cout << "🤖 Робот B. Начальный заряд: " << roboEnergyB << endl;
    chargeByReference(roboEnergyB);
    cout << "После pass by reference: " << roboEnergyB << " ✅ (изменился)" << endl << endl;

    cout << "🤖 Робот C. Начальный заряд: " << roboEnergyC << endl;
    chargeByAddress(&roboEnergyC);
    cout << "После pass by address: " << roboEnergyC << " ✅ (изменился)" << endl;

    return 0;
}
