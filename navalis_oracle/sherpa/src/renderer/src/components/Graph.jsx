import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';

const Graph = ({ data }) => {
  const svgRef = useRef();
  const [dimensions, setDimensions] = useState({ width: 400, height: 200 });

  // Set the fixed dimensions based on the main app window size (600x350)
  useEffect(() => {
    setDimensions({
      width: 400,  // Fixed width
      height: 200, // Fixed height
    });
  }, []);

  useEffect(() => {
    // Adjusted margin to give more space inside the window
    const margin = { top: 20, right: 10, bottom: 10, left: 20 };
    const width = dimensions.width - margin.left - margin.right;
    const height = dimensions.height - margin.top - margin.bottom;

    // Select the SVG element and set dimensions
    const svg = d3
      .select(svgRef.current)
      .attr('width', dimensions.width)
      .attr('height', dimensions.height)
      .style('border', '1px solid black');

    const { nodes, edges } = data;

    // Clear previous content from the SVG
    svg.selectAll('*').remove();

    // Find the bounding box for the nodes
    const xExtent = d3.extent(nodes, d => d.x);
    const yExtent = d3.extent(nodes, d => d.y);

    // Create scaling functions to fit nodes inside the viewBox
    const xScale = d3
      .scaleLinear()
      .domain(xExtent)
      .range([margin.left, width - margin.right]);

    const yScale = d3
      .scaleLinear()
      .domain(yExtent)
      .range([margin.top, height - margin.bottom]);

    // Create links (edges) between nodes
    svg
      .selectAll('line')
      .data(edges)
      .enter()
      .append('line')
      .attr('stroke', '#999')
      .attr('stroke-width', 1.5)
      .attr('x1', (d) => xScale(nodes.find((n) => n.id === d.source).x))
      .attr('y1', (d) => yScale(nodes.find((n) => n.id === d.source).y))
      .attr('x2', (d) => xScale(nodes.find((n) => n.id === d.target).x))
      .attr('y2', (d) => yScale(nodes.find((n) => n.id === d.target).y));

    // Create nodes (circles) with labels
    const node = svg
      .selectAll('g')
      .data(nodes)
      .enter()
      .append('g')
      .attr('transform', (d) => `translate(${xScale(d.x)}, ${yScale(d.y)})`);

    node
      .append('circle')
      .attr('r', 8)
      .style('fill', '#69b3a2');

    // Add labels to the nodes
    node
      .append('text')
      .attr('dy', '.35em') // Vertical alignment
      .attr('x', 12) // Position label to the right of the circle
      .style('fill', 'black')
      .text((d) => d.id);

  }, [data, dimensions]);

  return <svg ref={svgRef} />;
};

export default Graph;
