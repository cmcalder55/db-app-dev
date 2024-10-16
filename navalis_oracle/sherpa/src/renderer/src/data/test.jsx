export const data = {
  nodes: [
    { id: 1, x: 106, y: 128, name: "estate walkways", contents: [] },
    { id: 2, x: 175, y: 172, name: "sanitorium passage", contents: ["darkshrine"] },
    { id: 3, x: 244, y: 128, name: "aspirant's trial", contents: [] },
    { id: 4, x: 311, y: 128, name: "estate walkways", contents: ["darkshrine"] },
    { id: 5, x: 379, y: 40, name: "sanitorium passage", contents: ["darkshrine"] },
    { id: 6, x: 450, y: 128, name: "sepulchre halls", contents: ["darkshrine"] },
    { id: 7, x: 518, y: 128, name: "", contents: [""] },
    { id: 8, x: 621, y: 128, name: "", contents: [""] },
    { id: 9, x: 726, y: 40, name: "", contents: [""] },
    { id: 10, x: 691, y: 128, name: "", contents: [""] },
    { id: 11, x: 726, y: 216, name: "", contents: [] },
    { id: 12, x: 793, y: 128, name: "aspirant's trial", contents: [] }
  ],
  edges: [
    { source: 1, target: 2 },
    { source: 1, target: 3 },
    { source: 2, target: 3 },
    { source: 3, target: 4 },
    { source: 4, target: 5 },
    { source: 4, target: 6 },
    { source: 5, target: 6 },
    { source: 6, target: 5 },
    { source: 6, target: 7 },
    { source: 7, target: 8 },
    { source: 8, target: 9 },
    { source: 8, target: 11 },
    { source: 9, target: 10 },
    { source: 9, target: 12 },
    { source: 10, target: 9 },
    { source: 10, target: 11 },
    { source: 11, target: 10 },
    { source: 11, target: 12 }
  ]
}
