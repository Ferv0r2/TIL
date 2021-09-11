import React from "react";
import { StyleSheet, Text, View, Image } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <View style={styles.textContainer}>
        <Text style={[styles.BlueText, styles.BigText, styles.CenterText]}>
          스파르타 코딩클럽!!
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    //영역을 잡는 속성입니다. 따로 자세히 다룹니다.
    //flex: 1은 전체 화면을 가져간다는 뜻입니다
    flex: 1,
    //영역의 배경 색을 결정합니다
    backgroundColor: "#fff",
    //아래 두 속성은 영역 안의 컨텐츠들의 배치를 결정합니다.
    //flex를 자세히 다룰때 같이 자세히 다룹니다
    justifyContent: "center",
    alignContent: "center",
  },
  BlueText: {
    color: "blue",
  },
  BigText: {
    fontSize: 30,
  },
  CenterText: {
    alignSelf: "center",
  },
});
