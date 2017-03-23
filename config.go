package logpeck

import (
	"fmt"
	"github.com/BurntSushi/toml"
	"os"
)

type LogPeckConfig struct {
	Port          int32         `toml:"port"`
	MaxTaskNum    int32         `toml:"max_task_num"`
	DatabaseFile  string        `toml:"database_file"`
	PeckTaskLimit PeckTaskLimit `toml:"peck_task_limit"`
}

type PeckTaskLimit struct {
	MaxLinesPerSec int64 `toml:"max_lines_per_sec"`
	MaxBytesPerSec int64 `toml:"max_bytes_per_sec"`
}

var Config LogPeckConfig

func InitConfig(file *string) bool {
	Config = LogPeckConfig{
		Port:         7117,
		MaxTaskNum:   16,
		DatabaseFile: "meta.db",
	}

	if _, err := toml.DecodeFile(*file, &Config); err != nil {
		fmt.Fprintf(os.Stderr, "Parse config fail: %s.\n", err)
		return false
	}
	return true
}
