package interview

import (
	"time"
)

type Tag struct {
	Major int
	Minor int
	Patch int
}

type TestStatus int64

const (
	Passed TestStatus = iota
	Failed
)

type TestRun struct {
	Tag    Tag
	Status TestStatus
	Date   time.Time
}

type TestReport struct {
	FirstBrokenVersion string
	BreakTime          time.Time
	FixedVersion       string
	FixTime            time.Time
}

// GenerateTestReport
// We need to find:
// 1. moment in time when tests begin to FAIL and the first BROKEN version of the application
// 2. moment in time when tests begin to PASS and the first FIXED version of the application
//
// Example input:
// [
//
//	{"1.0.1", 1, "2023-09-14 10:30"},
//	{"1.1.0", 0, "2023-09-15 12:30"},
//	{"1.0.0", 0, "2023-09-13 10:36"}
//
// ]
func GenerateTestReport(testRuns []TestRun) TestReport {

	return TestReport{}
}
