import { Theme, useTheme } from '@mui/material/styles'
import Box from '@mui/material/Box'
import OutlinedInput from '@mui/material/OutlinedInput'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select, { SelectChangeEvent } from '@mui/material/Select'
import Chip from '@mui/material/Chip'

const ITEM_HEIGHT = 48
const ITEM_PADDING_TOP = 8
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
}

const getStyles = (region: string, regionCode: readonly string[], theme: Theme) => {
  return {
    fontWeight:
      regionCode.indexOf(region) === -1 ? theme.typography.fontWeightRegular : theme.typography.fontWeightMedium,
  }
}

export default function RegionSelect({
  regions,
  selectedRegions,
  onRegionChange,
}: {
  regions: string[]
  selectedRegions: string[]
  onRegionChange: (event: SelectChangeEvent<typeof selectedRegions>) => void
}) {
  const theme = useTheme()

  return (
    <FormControl sx={{ m: 1, width: 300 }}>
      <InputLabel id="demo-multiple-chip-label">Choose Netflix Region</InputLabel>
      <Select
        labelId="demo-multiple-chip-label"
        id="demo-multiple-chip"
        multiple
        value={selectedRegions}
        onChange={onRegionChange}
        input={<OutlinedInput id="select-multiple-chip" label="Chip" />}
        renderValue={(selected) => (
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {selected.map((value) => (
              <Chip key={value} label={value} />
            ))}
          </Box>
        )}
        MenuProps={MenuProps}
      >
        {regions.map((region) => (
          <MenuItem key={region} value={region} style={getStyles(region, selectedRegions, theme)}>
            {region}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  )
}
