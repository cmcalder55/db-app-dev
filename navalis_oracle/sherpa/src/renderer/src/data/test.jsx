export const data = {
    nodes: [{ id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }, { id: 5 }, { id: 6 },
            { id: 7 }, { id: 8 }, { id: 9 }, { id: 10 }, { id: 11 }, { id: 12 }],
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