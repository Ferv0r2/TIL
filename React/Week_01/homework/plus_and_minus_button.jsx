import React, { useState } from "react";
import { StyleSheet, View, Text } from "react-native";
import PlusButton from "./components/PlusButton";
import MinusButton from "./components/MinusButton";

export default function App() {
  const [state, setState] = useState(0);

  const Minus = () => {
    console.log("마이너스");
    setState(state - 1);
  };

  const Plus = () => {
    setState(state + 1);
  };

  return (
    <View style={styles.contianer}>
      <Text style={styles.count}>카운터 : {state}</Text>
      <View style={styles.buttonContainer}>
        <PlusButton Plus={Plus} />
        <MinusButton Minus={Minus} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  contianer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  count: {
    fontSize: 20,
  },
  buttonContainer: {
    marginTop: 50,
    flexDirection: "row",
  },
});
