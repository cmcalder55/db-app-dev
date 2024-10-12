import Select from 'react-select'

function ChooseLevel() {
  const options = [
    { value: 'Normal', label: 'Normal' },
    { value: 'Cruel', label: 'Cruel' },
    { value: 'Merciless', label: 'Merciless' },
    { value: 'Uber', label: 'Uber' }
  ]
  return (
    <Select
      defaultValue={{ value: '', label: 'Select Difficulty' }}
      options={options}
      styles={{
        control: (styles) => ({
          ...styles,
          backgroundColor: 'white'
        }),
        option: (styles, { isFocused, isSelected }) => ({
          ...styles,
          color: 'grey',
          backgroundColor:
          isSelected ? '#7bd69a':
          isFocused ? '#a3aaa5':
          undefined
        })
      }}
    />
  )
}
export default ChooseLevel
