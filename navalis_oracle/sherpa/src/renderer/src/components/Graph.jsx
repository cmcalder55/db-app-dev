import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';

const Graph = ({ data }) => {
  const svgRef = useRef();
  const [dimensions, setDimensions] = useState({ width: 460, height: 400 });

  useEffect(() => {
    const handleResize = () => {
      setDimensions({
        width: window.innerWidth - 60, // Adjust margin if needed
        height: window.innerHeight - 60,
      });
    };

    window.addEventListener('resize', handleResize);
    handleResize(); // Set initial dimensions

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  useEffect(() => {
    const margin = { top: 30, right: 30, bottom: 70, left: 60 };
    const width = dimensions.width - margin.left - margin.right;
    const height = dimensions.height - margin.top - margin.bottom;

    const svg = d3
      .select(svgRef.current)
      .attr('width', dimensions.width)
      .attr('height', dimensions.height)
      .style('border', '1px solid black');

    const { nodes, edges } = data;

    // Set initial positions for all nodes
    nodes.forEach((node, index) => {
      node.x = (index + 1) * (width / (nodes.length + 1)); // Distribute nodes evenly
      node.y = height / 2; // Center vertically
    });

    // Anchor the first and last nodes
    const firstNode = nodes[0]; // First node
    const lastNode = nodes[nodes.length - 1]; // Last node
    firstNode.fx = margin.left; // Fixed x position
    firstNode.fy = height / 2; // Fixed y position

    lastNode.fx = width - margin.right; // Fixed x position
    lastNode.fy = height / 2; // Fixed y position

    // Create a mapping of the edges to identify specific patterns
    const edgeMap = {};
    edges.forEach(edge => {
      if (!edgeMap[edge.source]) {
        edgeMap[edge.source] = [];
      }
      edgeMap[edge.source].push(edge.target);

      if (!edgeMap[edge.target]) {
        edgeMap[edge.target] = [];
      }
      edgeMap[edge.target].push(edge.source);
    });

    // Dynamically adjust positions for nodes connected in a square-like pattern
    nodes.forEach(node => {
      const connections = edgeMap[node.id] || [];
      if (connections.length === 3) {
        // Example: node 10 is connected to 9, 11, and one other (e.g., 12), adjust position accordingly
        const connectedNodes = connections.map(id => nodes.find(n => n.id === id));

        // Assume we're forming a square-like structure:
        if (connectedNodes.length === 3) {
          // Find center of the connected nodes and place the current node in the middle
          const avgX = d3.mean(connectedNodes.map(n => n.x));
          const avgY = d3.mean(connectedNodes.map(n => n.y));
          node.x = avgX;
          node.y = avgY - 50; // Adjust Y-position for forming a square
        }
      }
    });

    // Create the simulation
    const simulation = d3
      .forceSimulation(nodes)
      .force(
        'link',
        d3
          .forceLink()
          .id((d) => d.id)
          .distance(30) // Reduce link distance to bring nodes closer
      )
      .force('charge', d3.forceManyBody().strength(-10)) // Reduce repulsion between nodes
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('x', d3.forceX().strength(0.15)) // Gentle pull towards the center horizontally
      .force('y', d3.forceY().strength(0.1)); // Gentle pull towards the center vertically

    // Create links
    const link = svg.selectAll('.link').data(edges).enter().append('g').attr('class', 'link');

    link.append('line').attr('stroke', '#999');

    // Create nodes
    const node = svg
      .selectAll('.node')
      .data(nodes)
      .enter()
      .append('g')
      .attr('class', 'node');

    node.append('circle')
      .attr('r', 8)
      .style('fill', '#69b3a2');

    // Add labels to nodes
    node.append('text')
      .attr('dy', '.35em') // Vertical alignment
      .attr('x', 12) // Position to the right of the circle
      .style('fill', 'white')
      .text((d) => d.id);

    // Update positions on tick
    simulation.nodes(nodes).on('tick', () => {
      link
        .select('line')
        .attr('x1', (d) => d.source.x)
        .attr('y1', (d) => d.source.y)
        .attr('x2', (d) => d.target.x)
        .attr('y2', (d) => d.target.y);

      node.attr('transform', (d) => `translate(${d.x}, ${d.y})`); // Update position using transform
    });

    simulation.force('link').links(edges);
  }, [data, dimensions]);

  return <svg ref={svgRef} />;
};

export default Graph;
