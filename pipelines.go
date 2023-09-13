package interview

type Job struct {
	Name     string
	Duration int
	// passed, failed
	Status string
	Stage  string
}

type Pipeline struct {
	Jobs []Job
}

// ShortestPassedJob accepts list of Pipelines objects and returns the Job with the lowest Duration
// between Job's which status is "passed"
func ShortestPassedJob(pipelines []Pipeline) Job {

	return Job{}
}

// CalculatePipelineDuration accepts Pipeline object and returns it's duration
// Pipeline's - sum of all it's jobs durations
func CalculatePipelineDuration(pipeline Pipeline) int {

	return 0
}
